# SynthJail# SynthJail 🚀

![SynthJail Banner](https://via.placeholder.com/1200x400.png?text=SynthJail+-+Unlock+the+Future)  

**SynthJail** is a powerful CLI tool designed to interact with AI models using advanced jailbreaking prompts. It supports multiple AI platforms, including OpenAI, Claude AI, Gemini, and more, allowing users to push the boundaries of AI interaction.

---

## Features ✨
- **Multi-Model Support** – Compatible with OpenAI, Claude AI, Gemini, and others.
- **Jailbreaking Prompts** – Utilize predefined and customizable prompts.
- **User-Friendly CLI** – Simple and intuitive command-line interface.
- **Extensible Architecture** – Easily add support for new AI models.

---

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/variendarkgirl/SynthJail.git
   cd SynthJail
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys in `config.ini`:
   ```ini
   [API_KEYS]
   openai = your-openai-api-key
   claude = your-claude-api-key
   gemini = your-gemini-api-key
   ```

---

## Usage 🖥️

Run SynthJail with the following command:
```bash
synthjail --prompt-index 0 --model openai
```

### Arguments:
- `--prompt-index` – Index of the jailbreaking prompt to use.
- `--model` – Specify the AI model (e.g., `openai`, `claude`, `gemini`).

---

## Contributing 🤖

We welcome contributions! Here’s how you can help:
1. Fork the repository.
2. Add support for new AI models in the `models/` directory.
3. Submit a pull request with detailed documentation.

---

## License 📜

SynthJail is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Disclaimer ⚠️

This tool is intended for **educational and research purposes only**. Users must comply with the terms of service of the respective AI platforms.

---

