
import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from PRATIBHA import BOT_NAME, BOT_USERNAME, SACHIN, dev
from PRATIBHA.database.chats import add_served_chat
from PRATIBHA.database.users import add_served_user
from PRATIBHA.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_START,
   # START,
)


@dev.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("🤍")
        await asyncio.sleep(0.2)
        await accha.edit("💛")
        await asyncio.sleep(0.2)
        await accha.edit("🧡")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**❖ ʜᴇʏ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ... ! \n\n๏ ɪ ᴀᴍ [{BOT_NAME}](t.me/{BOT_USERNAME}) \n\n❍ ɪ ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ᴀɴᴅ ᴜsᴇғᴜʟ ʙᴏᴛ \n❍ ᴀɪ ʙᴀsᴇ sᴜᴘᴇʀ ғᴀsᴛ ᴄʜᴀᴛ ʙᴏᴛ \n❍ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴄᴏʟʟᴇᴄᴛ ʜᴀʀᴇᴍ ʙᴏᴛ \n\n❖ ᴜsᴇ ᴍᴇ /chatbot on/off & ғᴏʀ ᴍᴏʀᴇ /help .**""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    #    await add_served_user(m.from_user.id)
 #   else:
       # await m.reply_photo(
        #    photo=random.choice(IMG),
       #     caption=START,
        #    reply_markup=InlineKeyboardMarkup(HELP_START),
     #   )
    #    await add_served_chat(m.chat.id)


@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: SACHIN, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**❖ ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ꜰᴏʀ {BOT_NAME} !\n\n❍ /guess ➛ ᴛᴏ ɢᴜᴇss ᴄʜᴀʀᴀᴄᴛᴇʀ/n❍ /fav ➛ ᴀᴅᴅ ʏᴏᴜʀ ғᴀᴠʀᴀᴛᴇ/n❍ /trade ➛ ᴛᴏ ᴛʀᴀᴅᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs/n❍ /gift ➛ ɢɪᴠᴇ ᴀɴʏ ᴄʜᴀʀᴀᴄᴛᴇʀ ғʀᴏᴍ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ/n❍ /collection ➛ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ/n❍ /topgroups ➛ sᴇᴇ ᴛᴏᴘ ɢʀᴏᴜᴘs, ᴘᴘʟ ɢᴜᴇssᴇs ᴍᴏsᴛ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘs/n❍ /top ➛ ᴛᴏᴏ sᴇᴇ ᴛᴏᴘ ᴜsᴇʀs/n❍ /ctop ➛ ʏᴏᴜʀ ᴄʜᴀᴛ ᴛᴏᴘ/n❍ /changetime ➛ ᴄʜᴀɴɢᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴀᴘᴘᴇᴀʀ ᴛɪᴍᴇ/n❍ /chatbot ➛ ᴄʜᴀᴛʙᴏᴛ ᴏɴ - ᴏғғ ᴄᴏᴍᴍᴀɴᴅ/n❍ /ping ➛ ᴄʜᴇᴄᴋ ᴘɪɴɢ/n/n❖ ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ ɢʀᴏᴜᴘ.\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➠ /**""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )

  #########
      #  await add_served_user(m.from_user.id)
  #  else:
       # await m.reply_photo(
         #   photo=random.choice(IMG),
          #  caption="**๏ ʜᴇʏ ʙᴀʙʏ...\n\n๏ ᴘʟᴢ ᴜsᴇ ᴍᴇ ɪɴ ᴘᴠᴛ. ғᴏʀ ʜᴇʟᴏ ᴄᴍᴅs..!**",
          #  reply_markup=InlineKeyboardMarkup(HELP_BUTN),
       # )
       # await add_served_chat(m.chat.id)

#########

@dev.on_message(filters.command("IIIIIIIIIIrepo") & ~filters.bot)
async def repo(_, m: Message):
    await m.reply_text(
        text= f"""**❖ ᴀᴀ ɢʏᴀ ʀᴇᴘᴏ ʟᴇɴᴇ ʙᴏsᴅᴋ, ʏᴇ ᴠɪᴅᴇᴏ ᴅᴇᴋʜ ᴀᴜʀ ᴀᴘɴɪ ʀᴇᴘᴏ ʟᴇɴᴇ ᴋɪ ᴀᴀɢ ʙʜᴜᴊʜᴀ.**\n\n❖ https://x-hd.video/video/-aubree-valentine-switch-roles-fta-reality-kings.html """,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


#@dev.on_message(filters.new_chat_members)
#async def welcome(_, m: Message):
#    for member in m.new_chat_members:
     #   await m.reply_photo(photo=random.choice(IMG), caption=START)
          
