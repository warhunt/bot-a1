from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from .throttling import ThrottlingMiddleware

def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
