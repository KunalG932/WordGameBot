from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from word.database.db import add_user, get_user, add_group, get_group
from word import word

START_TEXT = """**👋 Hey {user}!

{bot} - Hi! I host games of word chain in Telegram groups.
Add me to a group to start playing games!
**"""

@word.on_message(filters.command(["start", "help"]) & filters.private)
async def start(client: Client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if not await get_user(user_id):
        await add_user(user_id, user_name, first_name)
    
    await message.reply_photo(
        photo="https://i.ibb.co/XktTk8f2/145d93c11b4e.jpg",
        caption=START_TEXT.format(
            user=message.from_user.mention,
            bot=(await client.get_me()).first_name
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("+ Add Me +", url="https://t.me/WordNWordRobot?startgroup=true"),
                ]
            ]
        )
    )

@word.on_message(filters.command("start") & filters.group)
async def start_group(client: Client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    if not await get_user(user_id):
        await add_user(user_id, user_name, first_name)

    if not await get_group(message.chat.id):
        await add_group(message.chat.id, message.chat.title)
    
    await message.reply_photo(
        photo="https://i.ibb.co/XktTk8f2/145d93c11b4e.jpg",
        caption=START_TEXT.format(
            user=message.from_user.mention,
            bot=(await client.get_me()).first_name
        )
    )