# vector-lite

- Status: Experimental
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

A small, dependency-free 2D/3D vector implementation for learning and lightweight prototypes. Supports addition, subtraction, scalar multiplication, magnitude, and normalization.

## How to use

```python
from main import Vector

v1 = Vector("2d", 2, 3)
v2 = Vector("2d", 0, 4)
v3 = Vector("3d", 2, 3, 4)
v4 = Vector("3d", 5, 1, 0)

assert (v1 + v2).x == 2
assert (v1 + v2).y == 7
assert (v3 + v4).z == 4

assert (v2 - v1).x == -2
assert (v2 - v1).y == 1

assert v1.scal_mult(2).x == 4
assert v3.scal_mult(3).z == 12

assert abs(v1.magnitude() - sqrt(13)) < 1e-9
assert abs(v3.magnitude() - sqrt(29)) < 1e-9
```

## Notes

Not a NumPy replacement. Just a tiny vector class for when you want to understand the math or need something lightweight.
