import asyncio
from threading import Thread
import time
from datetime import date
 
import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.loader import dp, bot
from bot.utils.misc import rate_limit

import bot.data.config as config

#@rate_limit(15, 'activate')
@dp.message_handler(Command('activate'))
async def active_turbo_button(message: types.Message):
    await message.answer("Включаю турбокнопку. Подождите немного...")

    result = turbo_button_on()
    if not result:
        await message.answer("Турбокнопка включена")
    else:
        await message.answer("Турбокнопка УЖЕ включена")

async def turbo_button_on():
    """
    Function for activating the turbo button. 
    Open chrome in headless mode, and go to the website to activate turbo button.
    """

    session = requests.Session()

    session.get(
        url="https://asmp.a1.by/asmp/LoginMasterServlet?userRequestURL=https%253A%252F%252Fmy.a1.by%252F&serviceRegistrationURL=&service=ISSA&wrongLoginType=false&cookie=skip&level=20",
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36"
        }
    )

    session.post(
        url="https://asmp.a1.by/asmp/ProcessLoginServlet/srv-aaa2-prod/srv-b2b1-prod?aaacookie=srv-aaa2-prod&eacookie=srv-b2b1-prod",
        data={
            "UserID": config.PHONE_NUMBER,
            "mobilePassword": config.PASSWORD,
        }
    )

    session.get("https://my.a1.by/")

    session.post(
        url="https://my.a1.by/work.html", 
        data={
            "sid3": session.cookies.get("WASESSION"),
            "user_input_timestamp": int(time.time() * 1000),
            "user_input_0": "_root/TPLAN/MOBILE_INTERNET",
        }
    )
    
    response = session.post(
        url="https://my.a1.by/work.html",
        data={
            "sid3": session.cookies.get("WASESSION"),
            "user_input_timestamp": int(time.time() * 1000),
            "user_input_0": "_next",
            "user_input_1": "DP1"
        }
    )

    if f"""23:59:59 {date.today().strftime("%d.%m.%Y")}""" in response.text:
        return False

    for _ in range(2):
        session.post(
            url="https://my.a1.by/work.html",
            data={
                "sid3": session.cookies.get("WASESSION"),
                "user_input_timestamp": int(time.time() * 1000),
                "user_input_0": "_next",
            }
        )

    return True