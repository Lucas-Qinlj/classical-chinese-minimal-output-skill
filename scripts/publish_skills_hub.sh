#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_PATH="$REPO_ROOT/skills/classical-chinese-minimal-output/SKILL.md"
GITHUB_REPO_URL="${GITHUB_REPO_URL:-https://github.com/Lucas-Qinlj/classical-chinese-minimal-output-skill}"
VISIBILITY="${VISIBILITY:-public}"
TAGS="${TAGS:-wenyan,classical-chinese,concise-writing,style}"

echo "Publishing skill from:"
echo "  $SKILL_PATH"
echo "To skills-hub with:"
echo "  visibility=$VISIBILITY"
echo "  github_repo=$GITHUB_REPO_URL"
echo "  tags=$TAGS"

npx -y @skills-hub-ai/cli publish "$SKILL_PATH" \
  --visibility "$VISIBILITY" \
  --github-repo "$GITHUB_REPO_URL" \
  --tags "$TAGS"
