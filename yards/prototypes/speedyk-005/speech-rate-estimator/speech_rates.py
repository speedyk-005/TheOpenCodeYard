"""
Estimated speech rate database expressed in syllables per second (SPS).

This module provides approximate articulation-rate values for various
languages based on publicly available studies and reports. These values
represent statistical averages from sampled speakers and are intended 
for estimation, modeling, and TTS applications. 

Data Sources (in order of original study relevance):

1. 2019 article data via Language Log discussion (Pellegrino et al.)
   - Discussion link: https://languagelog.ldc.upenn.edu/nll/?p=63362#:~:text=That%27s%20my%20point.-,Jerry%20Packard%20said%2C,-April%209%2C%202024
   - Provides calculated speech rates (syl/sec) for 17 languages, compiled by Dr. Pellegrino.

2. "Fastest Spoken Languages in the World" (Lingopie Blog, 2024)
   - Link: https://lingopie.com/blog/fastest-spoken-languages-in-the-world/
   - Original SPM measurements converted to SPS using: SPS = SPM / 60

3. "Languages in the USA: Speaking Rates per Minute" (Voices.com, 2022)
   - Link: https://www.voices.com/blog/languages-in-usa-speaking-rates-per-minute/
   - WPM values converted to SPS using: SPS = (WPM * average_syllables_per_word) / 60
"""

from typing import Literal

# Dictionary: Language code (ISO 639-1, 2 letters) → Syllables per Second (float)
# Ordered: original study → Lingopie → Voices.com (deduplicated)
LANGUAGES_ARTICULATION_RATE = {
    # 2019 study via Language Log discussion
    "ca": 7.07,  # Catalan
    "cm": 5.86,  # Mandarin (CMN)
    "de": 6.09,  # German
    "en": 6.34,  # English
    "eu": 7.54,  # Basque
    "fi": 7.17,  # Finnish
    "fr": 6.88,  # French
    "hu": 5.87,  # Hungarian
    "it": 7.16,  # Italian
    "ja": 8.03,  # Japanese
    "ko": 7.12,  # Korean
    "es": 7.73,  # Spanish
    "sr": 7.15,  # Serbian
    "th": 4.70,  # Thai
    "tr": 7.05,  # Turkish
    "vi": 5.30,  # Vietnamese

    # Lingopie Blog 2024 (languages not in 2019 dataset)
    "pt": 7.50,  # Portuguese
    "hi": 6.55,  # Hindi

    # Voices.com 2022 (remaining languages)
    "tl": 7.33,  # Tagalog
    "ru": 6.13,  # Russian
}

# Define valid personality types
PersonalityType = Literal[
    "enthusiastic",
    "analytical", 
    "concise",
    "neutral",
    "calm",
    "urgent",
    "authoritative",
    "friendly",
    "dramatic",
    "professional",
]

# Personality-based speech rate modifiers
PERSONALITY_SPEED: dict[PersonalityType, float] = {
    "enthusiastic": 1.15,    # 15% faster - excited, energetic
    "analytical": 0.85,      # 15% slower - thoughtful, precise
    "concise": 1.0,          # Normal speed - direct, to the point
    "neutral": 1.0,          # Normal speed - balanced
    "calm": 0.9,             # 10% slower - relaxed, soothing
    "urgent": 1.2,           # 20% faster - rushed, important
    "authoritative": 0.95,   # 5% slower - commanding, deliberate
    "friendly": 1.05,        # 5% faster - warm, approachable
    "dramatic": 0.8,         # 20% slower - exaggerated, theatrical
    "professional": 1.0,     # Normal speed - standard business
}


def get_lang_speech_rate(lang_code: str, personality: PersonalityType = "neutral") -> float:
    """Get the speech rate in syllables per second for a given language code.
    
    Args:
        lang_code: Two-letter ISO 639-1 language code (e.g., 'en', 'es', 'fr')
        personality: Personality type affecting speech speed modifier.
                     Defaults to "neutral".
    
    Returns:
        float: Speech rate in syllables per second. Returns 6.0 if language
               code is not found (global average fallback).
    
    Raises:
        ValueError: If personality type is not recognized.
    
    Example:
        >>> get_lang_speech_rate('es')
        7.73
        >>> get_lang_speech_rate('en', 'enthusiastic')
        7.29
        >>> get_lang_speech_rate('xx')  # Non-existent code
        6.0
    """
    # Validate personality type
    if personality not in PERSONALITY_SPEED:
        valid_personalities = ", ".join(sorted(PERSONALITY_SPEED.keys()))
        raise ValueError(
            f"Invalid personality '{personality}'. "
            f"Must be one of: {valid_personalities}"
        )
    
    # Get base speech rate for language with fallback
    base_rate = LANGUAGES_ARTICULATION_RATE.get(lang_code, 6.0)
    
    # Apply personality modifier
    modifier = PERSONALITY_SPEED[personality]
    adjusted_rate = base_rate * modifier
    
    # Apply reasonable bounds (3.0 to 10.0 SPS)
    MIN_RATE = 3.0
    MAX_RATE = 10.0
    return max(MIN_RATE, min(adjusted_rate, MAX_RATE))