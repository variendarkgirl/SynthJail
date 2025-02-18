import argparse
from synthjail.prompt_manager import PromptManager
from synthjail.config_manager import ConfigManager
from synthjail.logger import Logger
from synthjail.ai_models import OpenAI, Claude, Gemini

class CLI:
    def __init__(self):
        self.logger = Logger()
        self.config = ConfigManager()
        self.prompt_manager = PromptManager()

    def run(self):
        parser = argparse.ArgumentParser(description="SynthJail - AI Jailbreaking CLI Tool")
        parser.add_argument("--model", type=str, required=True, help="AI model to use (e.g., openai, claude, gemini)")
        parser.add_argument("--prompt", type=str, required=True, help="Prompt to use for jailbreaking")
        args = parser.parse_args()

        model = self._get_model(args.model)
        prompt = self.prompt_manager.load_prompt(args.model, args.prompt)

        if model and prompt:
            response = model.generate(prompt)
            self.logger.info(f"Response: {response}")
        else:
            self.logger.error("Invalid model or prompt.")

    def _get_model(self, model_name):
        if model_name == "openai":
            return OpenAI(self.config.get_api_key("openai"))
        elif model_name == "claude":
            return Claude(self.config.get_api_key("claude"))
        elif model_name == "gemini":
            return Gemini(self.config.get_api_key("gemini"))
        else:
            self.logger.error(f"Model '{model_name}' is not supported.")
            return None

if __name__ == "__main__":
    cli = CLI()
    cli.run()
