# DeterministicSpanFinder

Status: Archived
Origin: Extracted from chunklet
Main Language: Python
Accepting Contributions: No

---

## What it does

Find substring spans in text ignoring punctuation and non-alphanumeric characters. A deterministic alternative to regex — ~2x faster by avoiding backtracking.

## How to use

```python
from main import DeterministicSpanFinder

finder = DeterministicSpanFinder("Hello, world! Python3.10 is great.")
start, end = finder.find_span("Python310 is great")
print(finder.full_text[start:end])  # "Python3.10 is great"
```

## Notes

Extracted from [chunklet-py](https://github.com/speedyk-005/chunklet-py) (MIT). The original used this inside a chunking pipeline for LLM output parsing.
