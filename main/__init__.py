#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = "10264832" #config("API_ID", default=None, cast=int)
API_HASH = "95a5e1891b825a5070a2108cca075ca2" #config("API_HASH", default=None)
BOT_TOKEN = "7146007914:AAEbU2L0N43RKLsW8m48-WpTpoqfiH7zRe0" #config("BOT_TOKEN", default=None)
SESSION = "AQCcoQAAJCDwP8ioax_7rFLuzDH3QRm26uujP5GYHiMx0yBI64OgvsWZAKHJxjm_pzWjfluvHM2TI8v15GD7AZVOk0925uvi3DoAvH_JSr3B_WS-VSTTjYempQWlTYF3QQ2wb5Yqd-JX2gbdlvDWqEkaXCNqnOMuqskGsKz1sM33j0bz2OPga8MTBsl_7EyPgd6HamsUm2e7fcitD7VS0KAm2Vjf8OBb1Q8Dpq9QYsHcXmB6snp_um2Tnh3v8ozQcw7WOSdoKXrlddRaBPBAafrv2E0tAr6cs8-u-B-W0MeOpbRbrJM0L9fjnNaWibvXjfvETTo3XgGqvJvl6OdZFzkgnrhmoAAAAAGbB1LlAA" #config("SESSION", default=None)
FORCESUB = "okwithu" #config("FORCESUB", default=None)
AUTH = "1112773045" #config("AUTH", default=None)
SUDO_USERS = [1112773045,1975696269,5708998374]

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    # print(e)
    # logger.info(e)
    sys.exit(1)
