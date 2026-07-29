# Speech Rate Estimator

- Status: Active
- Main Language: Python
- Accepting Contributions: Yes

---

## What it does

Estimates the spoken duration of text for TTS synthesis. Counts syllables using Pyphen, applies language-specific speech rates, and adjusts for personality-based pacing. Auto-detects language if not provided.

## How to use

```bash
pip install -r requirement.txt
python main.py
```

## Dependencies

- `pyphen` — syllable counting
- `py3langid` — language auto-detection
- `syntok` — tokenization

## Notes

Speech rate data sourced from Pellegrino et al. (2019), Lingopie (2024), and Voices.com (2022). Supports 10 personality modifiers (enthusiastic, calm, urgent, etc.) and 20+ languages.