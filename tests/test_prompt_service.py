from services.prompt_service import PromptService


def test_prompt_creation():

    prompt = PromptService.build_content_prompt(
        business="bakery",
        audience="Students",
        emotion="Exciting",
        season="Summer",
        language="English",
        ai_mode="Creative",
    )

    assert "bakery" in prompt

    assert "Students" in prompt

    assert "Creative" in prompt
