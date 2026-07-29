# Undo Playground

- Status: Experimental
- Main Language: Python
- Accepting Contributions: No

---

## What it does

Dual-queue undo/redo playground using `LifoQueue`. Unlimited undo depth; redo limited to the last 5 undone actions.

## How to use

```bash
python main.py
```

Commands: `do('action')`, `undo()`, `redo()`, `exit()`

## Notes

Pure stdlib — no dependencies. Good for understanding stack-based undo/redo patterns.