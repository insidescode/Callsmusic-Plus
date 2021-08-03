# A Plugin From Daisyxmusic (Telegram bot project)
# Copyright (C) 2021  Inukaasith

from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["joingrp"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>You Need To Promote Me Admin To Use That Command</b> :p",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "NexaMusicAssistant" # F this

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"🌟 Zer0Byte 2.0 Assistant Joined 🌟 Don't Spam or Else I will f you!")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Zer0Byte 2.0 Assistant is already in your chat!</b> Don't use commands like a <b>kid</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"ERROR 404! <b>‼️ Flood Wait Error\n Sorry! user {user.first_name} couldn't join your group due to heavy join requests! Also make sure Zer0Byte Assistant account is not banned in your group. ✅"
            "\n\nOr you can manually add @{(await USER.get_me()).username} to your Group!</b> 😉",
        )
        return
    await message.reply_text(
            "<b>🌟 Zer0Byte 2.0 Assistant Joined 🌟</b>",
        )

# Remove Bot and Streamer Account From the group
@Client.on_message(filters.group & filters.command(["leavegrp"]))
@authorized_users_only
async def botleavegrp(client, message):
    await message.chat.leave()

@USER.on_message(filters.group & filters.command(["leavegrp"]))
async def strmleavegrp(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>🚫Oops! Zer0Byte 2.0 Assitant Can't Leave Right Now! May Be Floodwait🚫"
            "\n\nOr You Can Manually Remove @{(await USER.get_me()).username}</b>",
        )
        return
