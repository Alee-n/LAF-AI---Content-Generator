from services.ai_service import AIService
from services.prompt_service import PromptService


def generate_ai_content(
    business,
    audience,
    emotion,
    season,
    language,
    ai_mode
):

    service = AIService("openrouter")

    prompt = PromptService.build_content_prompt(
        business,
        audience,
        emotion,
        season,
        language,
        ai_mode
    )

    return service.generate(prompt)