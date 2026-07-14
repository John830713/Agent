# Specification

## Common commands

| Command | Description |
|---------|-------------|
| `git status` | Show working tree status |
| `git diff` | Show unstaged changes |
| `git log --oneline -10` | Show last 10 commits (one line each) |
| `git add <file>` | Stage changes |
| `git commit -m "<msg>"` | Commit staged changes |
| `git push` | Push to remote |

## Rules

- Only commit what the user explicitly asks for
- Never commit secrets or credentials
- Write concise commit messages describing the change
- Split commits by feature: one logical change per commit
- Commit whenever changes exist — better to over-commit and squash later than to miss a submission
