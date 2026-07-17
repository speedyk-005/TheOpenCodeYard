---
name: contribute-scrapt
description: Handle full deployment of scrap code or prototypes — user pastes code or provides a path, the agent handles the rest
version: 1.0.0
license: MIThe same as the project license
author: "speedyk-005"
tags:
  - scraps
  - prototypes
  - deploy
  - contribute
  - open-code-yard
  - the-open-codeyard
---

## Instructions

This skill handles the full workflow of adding a scrap or prototype to The Open CodeYard repository. The user provides either the code directly (paste) or a file path, and the agent takes care of everything: directory creation, README generation, README update, and commit.

### When to Use

- User says "add this scrap" or "deploy this prototype"
- User pastes code they want to contribute
- User provides a file path to their code
- User wants to contribute to The Open CodeYard but doesn't want to handle the structure themselves

### How to Use

The agent receives a piece of code (pasted or file path) and determines:

1. **Which yard it belongs to** — `scraps` or `prototypes`
   - `scraps/` — small utilities, snippets, one-off scripts, notes (< ~200 lines, single file)
   - `prototypes/` — larger experiments, proof-of-concepts, multi-file projects
2. **Creates the directory structure** — `yards/<yard>/<username>/<project-name>/`
3. **Writes the code file(s)** with appropriate naming
4. **Generates a minimal README.md** describing what it does
5. **Stages and commits** the changes
6. **Reminds the user to push** (never pushes automatically)

### Safety Rules

- **Always switch to a new branch** before making any changes. Never work directly on `main`. Name branches descriptively (e.g., `add/file-renamer`, `deploy/sql-filter`).
- **Never run dangerous commands** without asking first. This includes: `rm -rf`, `git push --force`, `git reset --hard`, `git checkout` with destructive flags, `git branch -D`. Always ask the user for confirmation.

### Yard Rules

- Keep projects under 5 MB total
- No `node_modules`, build artifacts, or binaries unless essential
- Code must be something the user can explain — not blind AI copy-paste
- If the user doesn't understand the code, ask them to learn it first

## Examples

**Example 1 — Pasting a script:**
```
User: here's a quick script i wrote for renaming files, add it
---code---
import os, sys
for f in os.listdir('.'):
    if f.endswith('.tmp'):
        os.rename(f, f.replace('.tmp', '.bak'))
---code---
Agent: 
   ✓ Created yards/scraps/speedyk-005/file-renamer/rename_script.py
   ✓ Created yards/scraps/speedyk-005/file-renamer/README.md
   ✓ Committed: feat: add file-renamer script
   ⚠  Don't forget to push when ready!
```

**Example 2 — Providing a file path:**
```
User: i have a prototype at ~/projects/sql-filter/ that i want to contribute
Agent: 
   ✓ Copied sql-filter/ → yards/prototypes/speedyk-005/sql-filter-dsl/
   ✓ Created yards/prototypes/speedyk-005/sql-filter-dsl/README.md
   ✓ Committed: feat: add sql-filter-dsl prototype
   ⚠  Don't forget to push when ready!
```

**Example 3 — User doesn't understand the code:**
```
User: here's this AI-generated thing, i don't really get it
Agent: I can't add code you can't explain. That's one of the yard rules.
Let's walk through it together first — what's it supposed to do?
```

## Limitations

- Works only within The Open CodeYard repository structure
- Cannot handle binary files or very large projects (> 5 MB)
- Cannot push automatically (user must push manually per project rules)
- Does not deploy to any external service — only commits to the repo
