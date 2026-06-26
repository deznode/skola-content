#!/usr/bin/env bash
#
# changelog-guard.sh — require a CHANGELOG.md update for every artifact touched.
#
# Mirrors the "changelog drift" job in .github/workflows/content-ci.yml, but runs
# locally on staged files via Lefthook (pre-commit). Each argument is a path
# (relative to repo root) to a staged file.
#
# Rule: if a commit stages any file under an artifact root (currently `courses/<slug>/`),
# that artifact's `courses/<slug>/CHANGELOG.md` must also be staged. Staging only
# the CHANGELOG.md (e.g. a typo fix) is always allowed — it is itself an artifact file.
#
# NOTE: blog artifacts are intentionally NOT gated yet — the `blog/` layout is still
# empty/undefined. Add `blog/<slug>` to artifact_root() once its publish shape lands.
#
# Exit 1 if any touched artifact is missing its CHANGELOG.md update, 0 otherwise.

set -euo pipefail

files=("$@")
[ "${#files[@]}" -gt 0 ] || exit 0

# Map a staged path to its artifact root, or empty string if it is not an artifact file.
artifact_root() {
  case "$1" in
    courses/*/*) printf '%s\n' "$1" | cut -d/ -f1-2 ;;
    *) printf '' ;;
  esac
}

# Collect the unique artifact roots that have staged changes.
roots=$(
  for f in "${files[@]}"; do
    artifact_root "$f"
  done | sort -u
)

missing=0
while IFS= read -r root; do
  [ -n "$root" ] || continue
  changelog="$root/CHANGELOG.md"

  staged_changelog=0
  for f in "${files[@]}"; do
    if [ "$f" = "$changelog" ]; then
      staged_changelog=1
      break
    fi
  done

  if [ "$staged_changelog" -eq 0 ]; then
    echo "✗ $root changed but $changelog was not updated/staged"
    missing=1
  fi
done <<EOF
$roots
EOF

if [ "$missing" -ne 0 ]; then
  echo ""
  echo "Every change to an artifact must be recorded in that artifact's CHANGELOG.md."
  echo "Add an entry under a dated heading (see an existing CHANGELOG.md), 'git add' it,"
  echo "then re-commit. Bypass once with: LEFTHOOK=0 git commit ...   (use sparingly)"
fi

exit "$missing"
