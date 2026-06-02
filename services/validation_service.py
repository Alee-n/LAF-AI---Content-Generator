ALLOWED_BUSINESSES = ["bakery", "restaurant", "travel", "convenience store"]

ALLOWED_AI_MODES = ["Creative", "Professional", "Minimal", "Viral"]

ALLOWED_LANGUAGES = ["English", "Japanese"]


def validate_business(business):

    if not business:

        return False

    return business.strip().lower() in ALLOWED_BUSINESSES


def validate_ai_mode(ai_mode):

    return ai_mode in ALLOWED_AI_MODES


def validate_language(language):

    valid_languages = ["English", "Japanese Style"]

    return language in valid_languages
