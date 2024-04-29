import asyncio
import importlib
import logging
import re
import sys
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client

import config
from PRATIBHA.modules import all_modules

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous


OWNER = config.OWNER_ID
# DEVS = config.SUDO_USERS | config.OWNER_ID


class SACHIN(Client):
    def __init__(self):
        super().__init__(
            name="SACHIN",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="PRATIBHA.modules"),
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.id = get_me.id
        self.name = get_me.mention
        self.username = get_me.username

    async def stop(self):
        await super().stop()


dev = Client(
    "Dev",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)

dev.start()

BOT_ID = config.BOT_TOKEN.split(":")[0]
x = dev.get_me()
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username
BOT_MENTION = x.mention
BOT_DC_ID = x.dc_id
