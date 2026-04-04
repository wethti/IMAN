# /save Skill

## Trigger
When user types `/save` or "save my work"

## Steps
1. Run `git status` to see what changed
2. Run `git add .` (or specific folders if scoped)
3. Generate a commit message based on file names + content diff
4. Run `git commit -m "[auto] <generated message>"`
5. Run `git push origin main`
6. Confirm to user: "Saved. Changes pushed: [list files]"

## Constraints
- If push fails, surface the error in plain English, not raw git output