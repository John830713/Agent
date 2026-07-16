# git — Rules & Notes

## Git rules

See `D:\Agent\AGENTS.md` → "Git and GitHub" section for:

- Commit workflow (status, diff, add, commit, push)
- Commit message style and splitting by feature
- Secrets protection
- PR creation guidelines
- `gh` usage for GitHub tasks

Also see `D:\Agent\AGENTS.md` → "Data sync" section for cross-machine sync conventions.

## Local conventions (this repo)

- Commit whenever changes exist — better to over-commit and squash later than to miss a submission
- Use `git revert` for public history; `git rebase -i HEAD~N` to squash before push
- Review `git diff --cached` before commit to avoid leaking secrets

