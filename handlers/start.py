import os

from pyrogram import Client, filters # Ik this is weird as this shit is already imported in line 6! anyway ... Fuck Off!
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2
from helpers.database import db, Database
from helpers.dbthings import handle_user_status
from config import LOG_CHANNEL, BOT_USERNAME, UPDATES_CHANNEL


@Client.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/start":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**#BOTSTARTED ** \n#NEWUSER **Started Zer0Byte 2.0!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>✨ Welcome {message.from_user.mention} !</b>

💭 Zer0Byte 2.0 **allows you** to **play music** on **groups** through the new **Telegram's voice chats**!

💡 **Find out** all the **Bot's commands** and how they **work*8 by clicking on the » ⚙️ **Help Menu** button!

📣 Powered By:  **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add Me To a Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚙️ Help Menu", callback_data="cbhelpmenu"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗃 Source Code", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/Zer0ByteOfficial"
                    ),
                    InlineKeyboardButton(
                        "Support", url="https://t.me/Zer0ByteSupport"
                    )
                ]
            ]
        )
    )


# Help Menu

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/help":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**#BOTSTARTED ** \n#NEWUSER **Started Zer0Byte 2.0!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>✨ Hellow {message.from_user.mention} !</b>

**Here is the Help Menu Zer0Byte 2.0!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❓How To Use Zer0Byte 2.0", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎼 Lyrics", callback_data="cbgetlyrics"
                    ),
                    InlineKeyboardButton(
                        "🔎 YT Search", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎶Music Downloader", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "📹YT Video Downloader", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Del CMDs", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "📌 Quotely", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/credits":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**#BOTSTARTED ** \n#NEWUSER **Started Zer0Byte 2.0!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} !</b>

__Note!__ ⚠️: This Project Is <b>Not Fully Owned By @Zer0ByteOfficial</b> !

Credits To,

<b><a href="https://github.com/CallsMusic">CallsMusic</a></b> - For Callsmusic !
<b>Mr Dark Prince</b>
<b>TheHamkercat</b>
<b>AbirHasan2005</b>
<b>DevsExpo</b>
<b>TeamDaisyX</b>
<b>N A C</b>

📣 Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔔 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Support", url="https://t.me/Zer0ByteSupport"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )   


@Client.on_message(command(["vc", f"vc@{BOT_USERNAME}"]) & other_filters)
async def vc(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/vc":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**#BOTSTARTED ** \n#NEWUSER **Started Zer0Byte 2.0!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    VC_LINK = f"https://t.me/{message.chat.username}?voicechat"
    await message.reply_text(
        f"""<b>Hellow 👋 {message.from_user.first_name} !</b>


             ⚡️  **Voice Chat Link** ⚡️


[Here Is Your Voice Chat Link](https://t.me/{message.chat.username}?voicechat)


ZER0BYTE™""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 Share Voice Chat Link", url=f"https://t.me/share/url?url=**Join%20Our%20Group%20Voice%20Chat%20😉%20%20{VC_LINK}%20❤️**"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔔 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "👥 Support", url="https://t.me/Zer0ByteSupport"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )

    
@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def search(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/search":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**#BOTSTARTED** \n#NEWUSER **Started Zer0Byte 2.0!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "YES", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "NO", callback_data="close"
                    )
                ]
            ]
        )
    )
