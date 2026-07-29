# Progress Bar

- Status: Active
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

Colored terminal progress bar with dynamic gradient, ETA, count, and stdout hijacking. Wraps any iterable and handles mixed progress/log output.

## How to use

```bash
pip install more-itertools stringcolor
python main.py
```

### Basic usage

```python
from main import ProgressBar
import time

for item in ProgressBar(range(100)):
    time.sleep(0.02)
```

### With log messages mid-progress

```python
with ProgressBar(range(150)) as bar:
    for i in bar:
        time.sleep(0.01)
        if i % 15 == 0:
            print(f"LOG: Milestone {i // 15 + 1}")
```

### Manual total for generators

```python
def items():
    for i in range(50):
        yield i

for item in ProgressBar(items(), total=50):
    time.sleep(0.05)
```

### Custom width and characters

```python
for item in ProgressBar(range(20), width=40, fill_char="=", empty_char="."):
    time.sleep(0.1)
```

## Dependencies

- `more-itertools`: `ilen()` for counting generators
- `stringcolor`: ANSI color gradient