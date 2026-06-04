from providers.provider_factory import ProviderFactory


class AIService:

    def __init__(
        self,
        provider_name="openrouter"
    ):

        self.provider = ProviderFactory.get_provider(
            provider_name
        )

    def generate(self, prompt):

        return self.provider.generate(prompt)