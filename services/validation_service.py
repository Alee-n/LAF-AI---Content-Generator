from constants.business_types import VALID_BUSINESSES
from constants.languages import VALID_LANGUAGES
from constants.ai_modes import VALID_AI_MODES


def validate_business(business):

    return business in VALID_BUSINESSES


def validate_language(language):

    return language in VALID_LANGUAGES


def validate_ai_mode(ai_mode):

    return ai_mode in VALID_AI_MODES