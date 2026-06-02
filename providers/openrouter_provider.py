from openai import OpenAI

from config import Config


class OpenRouterProvider:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1", api_key=Config.OPENROUTER_API_KEY
        )

    def generate(self, prompt):

        completion = self.client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[{"role": "user", "content": prompt}],
        )

        return completion.choices[0].message.content
