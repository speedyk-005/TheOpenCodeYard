# Undo Playground

- Status: Experimental
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

A simple CLI playground demonstrating undo/redo using `LifoQueue`. Max undo stack of 5.

## How to use

```bash
python main.py
```

Commands: `do('action')`, `undo()`, `redo()`, `exit()`

## Notes

Pure stdlib — no dependencies. Good for understanding stack-based undo/redo patterns.