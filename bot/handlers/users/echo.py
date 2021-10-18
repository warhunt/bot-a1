from aiogram import types
from bot.loader import dp

@dp.message_handler()
async def bot_echo(message: types.Message):

    text = message.text

    await message.answer(text)

