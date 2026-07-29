# Bot Project

- Status: Experimental
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

A rule-based chatbot using token matching and point-scoring to select the best answer. No AI, no APIs — just regex tokenization and a knowledge base.

## How to use

```bash
python main.py
```

Type a message. Words are tokenized and matched against known query tokens. The highest-scoring answer wins.

## Notes

Pure stdlib. Good for understanding basic NLP tokenization and rudimentary chatbot logic.