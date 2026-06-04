from openai import OpenAI

from config import Config

from providers.base_provider import BaseProvider

from exceptions.provider_errors import AIProviderError

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

class OpenRouterProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(

            base_url="https://openrouter.ai/api/v1",

            api_key=Config.OPENROUTER_API_KEY

        )

    @retry(

        stop=stop_after_attempt(3),

        wait=wait_exponential(
            multiplier=1,
            min=2,
            max=10
        )

    )

    def generate(self, prompt):

        try:

            completion = self.client.chat.completions.create(

                model="deepseek/deepseek-chat-v3-0324:free",

                messages=[

                    {

                        "role": "user",

                        "content": prompt

                    }

                ]

            )

            return completion.choices[0].message.content

        except Exception as e:

            error_text = str(e)

            if "429" in error_text:

                raise AIProviderError(

                    "Rate limit exceeded. Please try again shortly."

                )

            raise AIProviderError(

                f"OpenRouter Error: {error_text}"

            )