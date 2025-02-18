import os
from synthjail.logger import Logger

class PromptManager:
    def __init__(self):
        self.logger = Logger()
        self.prompts_dir = os.path.join(os.path.dirname(__file__), "../prompts")

    def load_prompt(self, model_name, prompt_name):
        prompt_file = os.path.join(self.prompts_dir, f"{model_name}_prompts.txt")
        if not os.path.exists(prompt_file):
            self.logger.error(f"Prompt file for '{model_name}' not found.")
            return None

        with open(prompt_file, "r") as file:
            for line in file:
                if line.startswith(f"{prompt_name}:"):
                    return line.split(":", 1)[1].strip()
        self.logger.error(f"Prompt '{prompt_name}' not found in {prompt_file}.")
        return None
