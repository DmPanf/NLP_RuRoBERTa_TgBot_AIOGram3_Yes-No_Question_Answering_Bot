# 🧠 Yes/No Question Answering Bot based on RuRoBERTa

Welcome to the **Yes/No Question Answering Bot** project! This bot is built using the `aiogram` library and leverages a fine-tuned model based on Russian SuperGLUE for answering yes/no questions. The bot can discern sentiment and provide answers based on user-provided context.

## 📚 Project Overview

This bot is designed to interact with users in Telegram and respond to their yes/no questions. It uses a fine-tuned model from the Russian SuperGLUE benchmark to understand the context of the questions and provide accurate answers.

### ✨ Features

- **Interactive**: The bot interacts with users in real-time, answering their yes/no questions.
- **Contextual Understanding**: The bot processes the context provided by the user and uses it to generate accurate answers.
- **Sentiment Detection**: The bot can discern positive and negative sentiments in the provided context.
- **HTML Formatting**: Responses are formatted with HTML to enhance readability in Telegram.

## 🚀 Getting Started

Follow these instructions to get a copy of the bot up and running on your local machine.

### 🛠 Prerequisites

- Python 3.7 or higher
- Telegram Bot API Token
- `aiogram` version 3
- `transformers` and `safetensors` libraries

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yes-no-question-bot.git
   cd yes-no-question-bot
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root directory with the following content:
   ```env
   TG_BOT_TOKEN=your-telegram-bot-token
   MODEL_DIRECTORY=./model
   ```

4. Make sure your model files are placed in the `MODEL_DIRECTORY` as specified in the `.env` file.

### 🔧 Usage

To start the bot, simply run the following command:

```bash
python bot.py
```

The bot will start polling and be ready to answer yes/no questions based on the provided context.

### 📝 Example Queries

Here are a few example queries you can use to test the bot:

- **Positive Sentiment:**
  ```
  Did you enjoy your day?\nIt was an amazing day filled with joy and laughter. Everything went perfectly.
  ```

- **Negative Sentiment:**
  ```
  Are you disappointed?\nI am very disappointed with the outcome. It didn’t turn out the way I expected.
  ```

- **Contextual Understanding:**
  ```
  Is this a dangerous animal?\nLions are wild animals known for their strength and potential danger to humans.
  ```

### 🧪 Testing

You can test the bot by interacting with it directly in Telegram or by using automated tests (not included in this version).

### 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

### 🛡 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### 🙏 Acknowledgements

- Thanks to the developers of `aiogram`, `transformers`, and `safetensors` for their powerful tools.
- Special thanks to the creators of Russian SuperGLUE for providing a valuable dataset for model fine-tuning.
