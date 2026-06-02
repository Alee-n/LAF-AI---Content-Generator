class PromptService:

    @staticmethod
    def build_content_prompt(

        business,

        audience,

        emotion,

        season,

        language,

        ai_mode

    ):

        return f"""

You are an expert marketing strategist.

Generate:

3 captions

3 hashtags

2 content ideas

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

If AI Mode is:

Creative:
Use imaginative and unique language.

Professional:
Use polished business language.

Minimal:
Keep content concise.

Viral:
Use strong hooks and engagement.

Clearly separate:

Captions

Hashtags

Ideas

"""