# Tasker

- Status: Experimental
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

A background task runner that executes a callable asynchronously in a daemon worker thread. Supports one-shot mode (`once=True`) and continuous mode via event signaling.

## How to use

```python
from main import Tasker

def my_task():
    return {"result": 42}

t = Tasker(my_task)
t.run()
print(t.latest_result)  # {"result": 42}
```

## Notes

The task function must accept zero arguments and return a `dict`. Uses threading primitives only — no external dependencies.
