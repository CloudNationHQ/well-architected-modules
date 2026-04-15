#!/bin/bash
# One-time script to backfill all open issues from terraform module repos into the WAM project board.
# Going forward, new issues are automatically added via .github/workflows/add-issue-to-project.yml

GH="gh"
JQ="jq"
PROJECT_ID="PVT_kwDOB0xSjc4AZLQa"

echo "Fetching all open issues from CloudNationHQ terraform module repos..."

PAGE=1
ALL_ISSUES="[]"

while true; do
  RESPONSE=$("$GH" api "search/issues?q=org:CloudNationHQ+is:issue+is:open&per_page=100&page=$PAGE")

  PAGE_ISSUES=$(echo "$RESPONSE" | "$JQ" '[.items[]
    | select(.repository_url | test("terraform-azure-|terraform-azuread-|terraform-databricks-"))
    | select(.repository_url | test("terraform-azure-wam") | not)
    | {id: .node_id, title: .title, repo: (.repository_url | split("/") | last)}]')

  ALL_ISSUES=$(echo "$ALL_ISSUES $PAGE_ISSUES" | "$JQ" -s 'add')

  TOTAL=$(echo "$RESPONSE" | "$JQ" '.total_count')
  if [ $((PAGE * 100)) -ge "$TOTAL" ]; then break; fi
  PAGE=$((PAGE + 1))
done

TOTAL_FOUND=$(echo "$ALL_ISSUES" | "$JQ" 'length')
echo "Found $TOTAL_FOUND issue(s) to add to the project board."
echo ""

echo "$ALL_ISSUES" | "$JQ" -r '.[] | "  \(.repo)\n    - \(.title)\n"'

read -r -p "Add all $TOTAL_FOUND issue(s) to the project board? (y/n) " CONFIRM
if [ "$CONFIRM" != "y" ]; then
  echo "Aborted."
  exit 0
fi

mapfile -t ALL_ISSUE_IDS < <(echo "$ALL_ISSUES" | "$JQ" -r '.[].id')

for issue_id in "${ALL_ISSUE_IDS[@]}"; do
  "$GH" api graphql -f query='
    mutation($project: ID!, $content: ID!) {
      addProjectV2ItemById(input: {projectId: $project, contentId: $content}) {
        item { id }
      }
    }' -f project="$PROJECT_ID" -f content="$issue_id"
done

echo "Done."
