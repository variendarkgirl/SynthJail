from .models.openai import OpenAIClient
from .models.claude import ClaudeClient
from .models.gemini import GeminiClient
from .config_manager import ConfigManager

class AITools:
    def _init_(self):
        self.config = ConfigManager()

    def chat(self, prompt: str, model: str) -> str:
        """Send a prompt to the specified AI model."""
        api_key = self.config.get_api_key(model)
        if not api_key:
            raise ValueError(f"API key for {model} not found in config.")

        if model == "openai":
            client = OpenAIClient(api_key)
        elif model == "claude":
            client = ClaudeClient(api_key)
        elif model == "gemini":
            client = GeminiClient(api_key)
        else:
            raise ValueError(f"Unsupported model: {model}")

        return client.chat(prompt)
