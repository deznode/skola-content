#!/usr/bin/env bash
#
# check-links.sh — fail on broken *relative* Markdown links in the given files.
#
# Mirrors the "broken internal link" job in .github/workflows/content-ci.yml, but
# runs locally on staged files via Lefthook (pre-commit). Each argument is a path
# (relative to repo root) to a .md/.mdx file. Only links of the form
# `[text](./relative/path)` are checked; absolute URLs, anchors-only (`#foo`), and
# mailto: links are ignored. A `#fragment` suffix on a relative link is stripped
# before the existence check.
#
# Exit 1 if any referenced target is missing, 0 otherwise.

set -euo pipefail

broken=0

for file in "$@"; do
  [ -f "$file" ] || continue
  dir=$(dirname "$file")

  # Extract the target of every relative link `](./something)`, strip the
  # `](./` prefix and trailing `)`. Process substitution keeps the loop in the
  # current shell so `broken` survives.
  while IFS= read -r target; do
    target=${target%%#*}          # drop any #anchor fragment
    [ -n "$target" ] || continue
    if [ ! -e "$dir/$target" ]; then
      echo "✗ broken link in $file -> ./$target"
      broken=1
    fi
  done < <(grep -oE '\]\(\./[^)]+\)' "$file" 2>/dev/null | sed -E 's/^\]\(\.\///; s/\)$//')
done

[ "$broken" -eq 0 ] || echo "Broken relative links found — fix the paths above before committing."
exit "$broken"
