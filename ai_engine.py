from openai import OpenAI

from config import Config

# OPENROUTER CLIENT

client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=Config.OPENROUTER_API_KEY
)


# AI CONTENT GENERATION


def generate_ai_content(business, audience, emotion, season, language, ai_mode):

    try:

        prompt = f"""

        You are an expert marketing strategist.

        Generate:

        3 short captions

        3 hashtags

        2 marketing content ideas

        for a {business} business.

        Audience:
        {audience}

        Emotion:
        {emotion}

        Season:
        {season}

        Language Style:
        {language}

        AI Mode:
        {ai_mode}

        If AI Mode is:

        Creative:
        Use imaginative and unique language.

        Professional:
        Use polished business-oriented language.

        Minimal:
        Keep captions very short and clean.

        Viral:
        Use hook-based high-engagement style.

        Clearly separate:
        Captions,
        Hashtags,
        and Ideas.

        """

        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[{"role": "user", "content": prompt}],
        )

        return completion.choices[0].message.content

    except Exception:

        return """

Captions:
1. Fresh flavors made for your perfect day.
2. Experience premium quality and modern vibes.
3. Taste something unforgettable today.

Hashtags:
#Marketing
#ContentCreation
#BrandGrowth

Ideas:
1. Create behind-the-scenes content.
2. Show customer reactions and experiences.

"""



