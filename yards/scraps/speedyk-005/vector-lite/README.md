# vector-lite

Status: Experimental
Main Language: Python
Accepting Contributions: Yes

---

## What it does

A small, dependency-free 2D/3D vector implementation for learning and lightweight prototypes. Supports addition, subtraction, scalar multiplication, magnitude, and normalization.

## How to use

```python
from main import Vector

v1 = Vector("2d", 2, 3)
v2 = Vector("2d", 0, 4)
print(v1 + v2)  # (2, 7)
print(v1.magnitude())  # ~3.606
```

## Notes

Not a NumPy replacement. Just a tiny vector class for when you want to understand the math or need something lightweight.
