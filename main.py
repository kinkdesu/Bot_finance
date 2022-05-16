from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "5202629950:AAEc5X3yMo9I4WZzGSklNVZu3OBWSHUGbxM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['Start'])
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton("Как дела?", callback_data="but_1")
    markup.add(but_1)
    but_2 = InlineKeyboardButton("Кто ты?", callback_data="but_2")
    markup.add(but_2)

    await bot.send_message(message.chat.id, "Привет! Привет!", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "but_1")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Дела нормально")

@dp.callback_query_handler(lambda c: c.data == "but_2")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Я телеграмм бот")

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.text.lower() == 'пока':
        await message.reply("Досвидули")


executor.start_polling(dp)
