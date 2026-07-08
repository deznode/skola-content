#!/usr/bin/env node
// check-mdx-syntax.mjs — fail if any course lesson .mdx doesn't compile as MDX/JSX.
//
// Mirrors the existing `validate-code` job's py_compile/mvn-compile parse checks
// (content-ci.yml), but for lesson MDX. Catches parser-desyncing authoring
// mistakes — most commonly a backslash-escaped double quote inside a plain JSX
// attribute (e.g. `note="...\"..."`), which JSX does NOT treat as an escape: the
// `\` is literal, so the following `"` ends the attribute early and desyncs the
// rest of the tag.
//
// Without this check a malformed lesson still lands on `main` clean, and only
// fails later when apps/web runs Velite — which silently drops the lesson from
// the catalog (404 at runtime) instead of failing the build. See PR #9
// (tailwind-from-scratch lessons 22 + 23).
//
// Usage: node scripts/check-mdx-syntax.mjs
// Requires @mdx-js/mdx + remark-directive to be installed (CI installs them
// transiently; this repo has no package.json of its own).
//
// remarkDirective MUST be passed to compile() — it's the same plugin
// apps/web's Velite config wires in (see apps/web/velite.config.ts). Without
// it, a plain compile() misparses legitimate `:::callout{type=tip}` directive
// blocks (the `{type=tip}` attribute shorthand isn't valid bare MDX/JS) and
// throws a false positive on content Velite compiles just fine.
import { compile } from "@mdx-js/mdx";
import remarkDirective from "remark-directive";
import { readFile, readdir } from "node:fs/promises";
import path from "node:path";

function stripFrontmatter(content) {
  return content.replace(/^---\n[\s\S]*?\n---\n?/, "");
}

// Portable recursive walk for lesson MDX under courses/<slug>/lessons/<NN-slug>/*.mdx.
// Avoids fs.promises.glob (Node 22+ only) so this runs on the Node 20 CI pins elsewhere.
async function* findLessonMdx(root) {
  let coursesEntries;
  try {
    coursesEntries = await readdir(path.join(root, "courses"), { withFileTypes: true });
  } catch {
    return;
  }
  for (const course of coursesEntries) {
    if (!course.isDirectory()) continue;
    const lessonsDir = path.join(root, "courses", course.name, "lessons");
    let lessonDirs;
    try {
      lessonDirs = await readdir(lessonsDir, { withFileTypes: true });
    } catch {
      continue;
    }
    for (const lesson of lessonDirs) {
      if (!lesson.isDirectory()) continue;
      const lessonPath = path.join(lessonsDir, lesson.name);
      const files = await readdir(lessonPath, { withFileTypes: true });
      for (const file of files) {
        if (file.isFile() && file.name.endsWith(".mdx")) {
          yield path.join(lessonPath, file.name);
        }
      }
    }
  }
}

let failures = 0;

for await (const file of findLessonMdx(process.cwd())) {
  const raw = await readFile(file, "utf8");
  const body = stripFrontmatter(raw);
  try {
    await compile(body, { jsx: true, remarkPlugins: [remarkDirective] });
  } catch (e) {
    failures++;
    console.error(`✖ ${file}`);
    console.error(`  ${e.message.split("\n")[0]}`);
  }
}

if (failures > 0) {
  console.error(`\n${failures} lesson(s) failed MDX syntax validation.`);
  process.exit(1);
}
console.log("All lesson MDX files compile cleanly.");
