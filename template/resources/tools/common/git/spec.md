# Specification

## Common commands

| Command | Description |
|---------|-------------|
| `git status` | Show working tree status |
| `git diff` | Show unstaged changes |
| `git log --oneline -10` | Show last 10 commits |
| `git add <file>` | Stage changes |
| `git restore --staged <file>` | Unstage changes |
| `git commit -m "<msg>"` | Commit staged changes |
| `git commit --amend -m "<msg>"` | Amend last commit |
| `git push` | Push to remote |

## Rules

- Commit any change that exists; better to over-commit and squash later than to miss one
- Never commit secrets or credentials
- Write concise commit messages describing the change
- Split logical changes into separate commits
- Do NOT push unless the user explicitly says so
