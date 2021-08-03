from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from callsmusic.callsmusic import client as USER
from config import BOT_USERNAME, UPDATES_CHANNEL

# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# Player Control Callbacks

@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**Here is The Control Menu Of Zer0Byte 2.0 Player!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏭", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔇 Mute", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "🔊 Unmute", callback_data="cbunmute"
                    )
                ]
            ]
        )
    )


# Start callback 

@Client.on_callback_query(filters.regex("cbstart"))
async def startcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ Welcome {query.message.from_user.mention} !</b>

💭 Zer0Byte 2.0 **allows** you to **play music** on groups through the new **Telegram**'s voice chats!

💡 **Find out** all the **Bot's commands** and how they **work** by Clicking on » 📚 Help Menu!

Made with ❤️ **@{UPDATES_CHANNEL}**""",
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
                        "🔔 Updates", url=f"https://t.me/Zer0ByteOfficial"
                    ),
                    InlineKeyboardButton(
                        "👥 Support", url="https://t.me/Zer0ByteSupport"
                    )
                ]
            ]
        )
    )
    

# Help Callback Menu

@Client.on_callback_query(filters.regex("cbhelpmenu"))
async def cbhelpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ Hellow {query.message.from_user.mention} !</b>

**Help Menu Of Zer0Byte 2.0!**""",
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
                        "🔩 YT HELP", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎵Music Downloader", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "📹YT Video Downloader", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑Delete Commands", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "🔮 Quotely", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )

# How to Use Module Help

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbhowtouse(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>How To Use Zer0Byte 2.0?</b>

**Setting Up Zer0Byte 2.0:**
    1. Add **{BOT_USERNAME}** Bot and @{(await USER.get_me()).username} To Your Group! (Send `/joingrp` to your group! Streamer Will Automatically join)
    2. Give Admin To **{BOT_USERNAME}** and **@{(await USER.get_me()).username}** !

 
**Using Player Commands:**
    1. **Group Admin Only Commands 🛠 ,**
     - `/play` - Reply to supported url, Reply to Audio File or Send `/play` with [Supported Url](https://ytdl-org.github.io/youtube-dl/supportedsites.html)
       **Example:** `/play https://www.youtube.com/watch?v=ALZHF5UqnU4`
        
     - `/nplay` - Play Song by Name. (Currenty Supported for Youtube Only)
       **Example:** `/nplay Death of a Hero`
    
     - `/skip` - Skip currenly playing song.
    
     - `/pause` - Pause currently playing song.
    
     - `/resume` - Resume currently pushed song.
    
     - `/mute` - Mutes Streamer.
    
     - `/unmute`- Unmutes streamer.
     
     - `/end` - Stop playing and leaves the voice chat.
    
     - `/joingrp` - To Add Streamer Account To Your Group.
    
     - `/leavegrp` - To Remove Streamer Account From Your Group.
     
     - `/control` - To Control the Streamer Account in VC by Buttons. (Like pause, resume, skip etc.)
     
    2. **Other Commands,**
     - `/vc` - To Get and Share Voice Chat Link. (Public Groups Only)


**Supported Url List:** https://ytdl-org.github.io/youtube-dl/supportedsites.html

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Supported Url List", url="https://ytdl-org.github.io/youtube-dl/supportedsites.html"
                    ),
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        ),
        disable_web_page_preview = True
    )


# Lyrics Module Help

@Client.on_callback_query(filters.regex("cbgetlyrics"))
async def cbgetlyrics(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Zer0Byte 2.0 Lyrics  </b>

**Feature:** Get Lyrics For Provided Song Name!

**Usage:**
    - Send Your Song Name with `/lyrics` command.

**Example:** `/lyrics Carry me away`

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Yt Search Module Help

@Client.on_callback_query(filters.regex("cbytsearch"))
async def cbytsearch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Zer0Byte 2.0 YT Search</b>

**Feature:** Search Youtube Videos Inline or Using a Command!

**Usage:**
    1. For Inline Search Feature,
     - Type `@{BOT_USERNAME}` in any chat then type ` `(space) and search.
    
    2. For Search Via Command,
     - Send `/ytsearch` command with your keyword.

**Example:**
    1. Example For Inline Search
     - `@{BOT_USERNAME} faded`
    
    2. Example For Search via Command
     - `/ytsearch faded`

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
    
    
# Music Downloader Help

@Client.on_callback_query(filters.regex("cbmusicdown"))
async def cbmusicdown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Zer0Byte 2.0 YT Music</b>

**Feature:** Download Music As Audio From YouTube, Saavn, Deezer

**Usage:**
    1. For Youtube Audio Download,
      - Send Your Song Name with `/yts` command.
    
    2. For Saavn Audio Download,
      - Send Your Song Name with `/saavn` command.
    
    3. For Deezer Audio Download,
      - Send Your Song Name with `/deezer` command.

**Example:**
    1. Example For Youtube Audio Download,
      - `/yts alone`
    
    2. Example For Saavn Audio Download,
      - `/saavn faded`
    
    3. Example For Deezer Audio Download,
      - `/deezer unity`

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# YT Video Downloader Help

@Client.on_callback_query(filters.regex("cbytviddown"))
async def cbytviddown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Zer0Byte 2.0 YT Video Downloader</b>

**Feature:** Download Youtube Videos For Provided Name!

**Usage:**
    - Send Your Youtube Video Name with `/ytvid` command.

**Example:** `/ytvid faded`

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Delete Command Help

@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Zer0Byte 2.0 Delete CMDs</b>

**Feature:** Delete Every Commands Sent By Users to Avoid Spam in Your Group!

**Usage:**
    1. To Turn On This,
      - Send `/delcmd on` command.
    
    2. To Turn Off This,
      - Send `/delcmd off` command.

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Quotely Help

@Client.on_callback_query(filters.regex("cbquotely"))
async def cbquotely(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Zer0Byte 2.0 Quotely</b>

**Feature:** Quote Messages Like Quotely Bot!

**Usage:**
    1. To Quote One Message,
      - `/q` reply to a text message
      
    2. To Quote More Than One Message,
      - `/q` [Integer] reply to a text message
     
    3. To Quote Message with Reply
      - `/q r` reply to a text message

**Example:**
    1. Example Quote One Message,
      - `/q` reply to a text message
      
    2. Example Quote More Than One Message,
      - `/q 2` reply to a text message
     
    3. Example Quote Message with Reply,
      - `/q r` reply to a text message

📣Powered By: **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "←", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
