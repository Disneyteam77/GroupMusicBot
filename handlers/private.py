from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Doreamonfans](https://t.me/doreamonfans1).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/doreamonfans1")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/disneyteamchat"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/disneygrou"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add assistant bot to Group ➕", url="https://t.me/doreamonfans2"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/disneygrou")
                ]
            ]
        )
   )


