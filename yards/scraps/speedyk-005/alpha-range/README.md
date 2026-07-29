# Alpha Range

- Status: Experimental
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

Yield letters like `range()` does numbers. Supports start, stop, and step.

## How to use

```python
from main import alpha_range

for ch in alpha_range("a", "z", 2):
    print(ch)  # a, c, e, ...
```

## Notes

Uses `ord()`/`chr()` under the hood. Pure stdlib.