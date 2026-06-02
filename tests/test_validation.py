from services.validation_service import (
    validate_business,
    validate_ai_mode,
    validate_language,
)


def test_validate_business():

    assert validate_business("bakery") is True
    assert validate_business("restaurant") is True
    assert validate_business("travel") is True

    assert validate_business("hacker") is False


def test_validate_ai_mode():

    assert validate_ai_mode("Creative") is True
    assert validate_ai_mode("Professional") is True

    assert validate_ai_mode("Unknown") is False


def test_validate_language():

    assert validate_language("English") is True
    assert validate_language("Japanese Style") is True

    assert validate_language("French") is False
