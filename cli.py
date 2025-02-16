import argparse
import configparser
from pathlib import Path
from .prompts import get_jailbreak_prompt
from .models.openai import chat_with_openai
from .models.claude import chat_with_claude
from .models.gemini import chat_with_gemini

# Load API keys from config.ini
config = configparser.ConfigParser()
config.read(Path(_file_).parent / "config.ini")

def main():
    parser = argparse.ArgumentParser(description="Jailbreaking CLI Tool for Multiple AI Models")
    
    # Add arguments
    parser.add_argument(
        "--prompt-index",
        type=int,
        required=True,
        help="Index of the jailbreak prompt to use."
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        choices=["openai", "claude", "gemini", "copilot"],
        help="AI model to use."
    )
    
    args = parser.parse_args()
    
    try:
        # Get the jailbreaking prompt
        prompt = get_jailbreak_prompt(args.prompt_index)
        print(f"Using prompt: {prompt}")
        
        # Get the API key
        api_key = config["API_KEYS"][args.model]
        
        # Call the appropriate model
        if args.model == "openai":
            response = chat_with_openai(prompt, api_key)
        elif args.model == "claude":
            response = chat_with_claude(prompt, api_key)
        elif args.model == "gemini":
            response = chat_with_gemini(prompt, api_key)
        elif args.model == "copilot":
            response = "Copilot integration not yet implemented."
        
        print(f"Response:\n{response}")
    
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if _name_ == "_main_":
    main()
