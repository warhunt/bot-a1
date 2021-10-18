import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHROME_WEBDRIVER_PATH = "./chromedriver/chromedriver.exe"

WEBSITE_URL = "https://asmp.a1.by/asmp/LoginMasterServlet?userRequestURL=https%253A%252F%252Fmy.a1.by%252F&serviceRegistrationURL=&service=ISSA&wrongLoginType=false&cookie=skip&level=20"

PHONE_NUMBER = os.getenv("PHONE_NUMBER")

PASSWORD = os.getenv("PASSWORD")

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'

WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'

WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'

WEBAPP_PORT = int(os.getenv('PORT'))