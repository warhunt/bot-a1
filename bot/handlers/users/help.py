from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from bot.loader import dp
from bot.utils.misc import rate_limit

@rate_limit(15, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/activate - Активировать турбокнопку',
        '/help - Показать список доступных команд',
    ]
    await message.answer('\n'.join(text))
