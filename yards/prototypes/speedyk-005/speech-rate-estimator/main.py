from pyphen import Pyphen
from py3langid.langid import LanguageIdentifier, MODEL_FILE
from syntok.tokenizer import Tokenizer

from speech_rates import get_lang_speech_rate, PersonalityType


# Create a language identifier to auto-detect language if not provided
IDENTIFIER = LanguageIdentifier.from_pickled_model(MODEL_FILE, norm_probs=True)


def estimate_speech_duration(
    text: str,
    lang: str | None = None,
    personality: PersonalityType = "neutral"
) -> float:
    """
    Estimate the spoken duration of a text for TTS synthesis.

    The function counts syllables in the text using Pyphen, applies a language-
    specific speech rate, and adjusts for natural pauses. If the language code is 
    not provided, it will be auto-detected using py3langid. Longer language codes 
    are truncated to their first two letters to match supported ISO 639-1 codes.

    A fallback estimate is used if syllable counting fails, assuming ~1.2 syllables
    per token.

    Args:
        text (str): The text to estimate duration for.
        lang (str | None): Optional ISO 639-1 language code. Auto-detected if None.
        personality (PersonalityType): Speech style affecting rate (default 'neutral').

    Returns:
        float: Estimated duration in seconds, including a buffer for natural pauses.
    """
    # Tokenize text and extract token values
    words = [token.value for token in Tokenizer().tokenize(text)]

    # Auto-detect language if not provided
    if lang is None:
        lang, _ = IDENTIFIER.classify(text[:500])

    # Normalize language code to 2 letters if longer
    if len(lang) > 2:
        lang = lang.split("_")[0][:2]

    try:
        # Count syllables using Pyphen; may fail if language data is missing
        dic = Pyphen(lang=lang)
        syllable_count = sum(dic.inserted(word).count('-') + 1 for word in words)
    except Exception:
        # Fallback estimate if Pyphen fails
        syllable_count = len(words) * 1.2

    # Calculate duration using language-specific speech rate
    sps = get_lang_speech_rate(lang, personality)
    return syllable_count / sps * 1.15


if __name__ == "__main__":
    # Example with multiple languages and personalities
    examples = [
        ("Hello world, this is a test sentence.", "en", "neutral"),
        ("Hola mundo, esto es una prueba.", "es", "enthusiastic"),
        ("Ceci est une phrase de test.", "fra", "calm"),  # longer code will be normalized
        ("Dies ist ein Testsatz.", None, "professional"),  # auto-detect
    ]

    for text, lang, personality in examples:
        duration = estimate_speech_duration(text, lang, personality)
        print(f"Text: {text}\nLang: {lang}, Personality: {personality}, Duration: {duration:.2f} sec\n")