from providers.openrouter_provider import OpenRouterProvider
from providers.openai_provider import OpenAIProvider
from providers.claude_provider import ClaudeProvider


class ProviderFactory:

    @staticmethod
    def get_provider(provider_name):

        if provider_name == "openrouter":
            return OpenRouterProvider()

        elif provider_name == "openai":
            return OpenAIProvider()

        elif provider_name == "claude":
            return ClaudeProvider()

        raise ValueError(
            f"Unknown provider: {provider_name}"
        )