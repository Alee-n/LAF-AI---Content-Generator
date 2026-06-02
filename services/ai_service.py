from providers.openrouter_provider import OpenRouterProvider


class AIService:

    def __init__(self):

        self.provider = OpenRouterProvider()

    def generate(self, prompt):

        return self.provider.generate(prompt)
