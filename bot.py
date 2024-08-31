import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

from model import load_model_and_tokenizer
from predict import predict_answer

# Загрузка переменных окружения и инициализация бота
load_dotenv()

TOKEN = os.getenv('TG_BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Инициализация маршрутизатора
router = Router()
dp.include_router(router)

# Загрузка модели и токенизатора
model, tokenizer, device = load_model_and_tokenizer()

# Обработка команды /start
@router.message(Command("start"))
async def send_welcome(message: Message):
    sms = "\nЯ бот для обработки <b>[yes/no]</b> вопросов на основе данных из <b>Russian SuperGLUE</b>.\nВведите ваш вопрос и текст! 👀"
    await message.answer(f"👋 <b>Привет!</b> {sms}", parse_mode="HTML")

# Обработка текстовых сообщений
@router.message()
async def handle_message(message: Message):
    try:
        # Предполагаем, что вопрос и текст разделены символом новой строки
        question, passage = message.text.split('\n', 1)
        answer = predict_answer(question, passage, model, tokenizer, device)
        await message.answer(f"🪬 <b>Question:</b> {question}\n💎 <b>Passage:</b> {passage}\n♻️ <b>Answer:</b> {answer}", parse_mode="HTML")
    except ValueError:
        sms = "🛟 Пожалуйста, отправьте вопрос и текст через разделитель '\\n' (например, вопрос на одной строке, текст на другой)."
        await message.answer(sms)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
