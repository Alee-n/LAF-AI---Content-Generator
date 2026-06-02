from services.ai_service import AIService


def generate_ai_content(business, audience, emotion, season, language, ai_mode):

    service = AIService()

    prompt = f"""

    You are an expert marketing strategist.

    Generate:

    3 captions

    3 hashtags

    2 ideas

    Business:
    {business}

    Audience:
    {audience}

    Emotion:
    {emotion}

    Season:
    {season}

    Language:
    {language}

    AI Mode:
    {ai_mode}

    """

    return service.generate(prompt)
