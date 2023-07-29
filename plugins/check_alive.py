import time
import datetime
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CMD = ["/"]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    # Calculate the elapsed time since the start
    current_time = time.time()
    elapsed_time = current_time - start_time

    # Convert elapsed_time to a human-readable format
    elapsed_time_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))


    # Create the inline keyboard with two buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔁 Follow 🔁", url="https://t.me/CinemaVenoOfficial"),
                InlineKeyboardButton("🦋 Support 🦋", url="https://t.me/HexaSupportOfficial")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://i.imgur.com/DLVUuPk.jpeg",
        caption=f"┌─❖\n"
f"│「 𝗛𝗶  」\n"
f"└┬❖\n"
f"┌┤❖ 𝙃𝙚𝙡𝙡𝙤, {message.from_user.first_name}\n"
f"│└────────────┈ ⳹\n"
f"│✑ 𝙈𝙮𝙨𝙚𝙡𝙛:- 📍 <a href=https://t.me/Hexa_md_BOT>Ｈｅｘａ</a>\n"
f"│✑ 𝙑𝙚𝙧𝙨𝙞𝙤𝙣:- ♻️{get_bot_version()}\n"
f"│✑ 𝘼 𝙗𝙤𝙩 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮:- <a href=https://t.me/CinemaVenoOfficial>ᶜᵛᵒ</a>\n"
f"│✑ 𝘽𝙤𝙩 𝙍𝙪𝙣𝙩𝙞𝙢𝙚:- 🛰️{elapsed_time_formatted}\n"
f"└───────────────┈ ⳹",
        reply_markup=keyboard
    )




    
@Client.on_message(filters.command("menu", CMD))
async def help(_, message):
    # Get user's first name and bot version
    user_first_name = message.from_user.first_name
    bot_version = get_bot_version()

    # Get the current date, month, and year
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_month = datetime.datetime.now().strftime("%B")
    current_year = datetime.datetime.now().strftime("%Y")

    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    await message.reply_photo(
        photo="https://i.imgur.com/QiqadrP.jpeg",
        text ="╭━〔 HEXA 〕━◉\n"
        f"┃╭━━━━━━━━━━━━━━◉\n"
        f"┃┃ User:- {message.from_user.first_name}\n"
        "┃┃ Owner:- <a href=https://t.me/CinemaVenoOfficial>CinemaVenoOfficial</a>\n"
        f"┃┃ Version:- {get_bot_version()}\n"
        "┃┃ Prefix: /\n"
        f"┃┃ Mode:- Public\n"
        f"┃┃ Date:- {current_date}\n"
        f"┃┃ Time:- {current_time}\n"
        "┃╰━━━━━━━━━━━━━◉\n"
        "┃╭────────────···\n"
        "┃┠─═❮   FILTER   ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /filter\n"
        "┃╏  /filters\n"
        "┃╏  /del\n"
        "┃╏  /delall\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "┃╭────────────···\n"
        "┃┠─═❮  GROUP  ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /connect\n"
        "┃╏  /disconnect\n"
        "┃╏  /connections\n"
        "┃╏  /settings\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "┃╭────────────···\n"
        "┃┠─═❮  ADMIN  ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /mute\n"
        "┃╏  /tmute\n"
        "┃╏  /unmute\n"
        "┃╏  /pin\n"
        "┃╏  /unpin\n"
        "┃╏  /promote\n"
        "┃╏  /demote\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "┃╭────────────···\n"
        "┃┠─═❮ INFO ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /alive\n"
        "┃╏  /ping\n"
        "┃╏  /id\n"
        "┃╏  /info\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "┃╭────────────···\n"
        "┃┠─═❮    OWNER    ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /leave\n"
        "┃╏  /enable\n"
        "┃╏  /disable\n"
        "┃╏  /invite\n"
        "┃╏  /ban\n"
        "┃╏  /unban\n"
        "┃╏  /broadcast\n"
        "┃╏  /users\n"
        "┃╏  /chats\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "┃╭────────────···\n"
        "┃┠─═❮ 𝗦𝗘𝗔𝗥𝗖𝗛 ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /imdb\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "┃╭────────────···\n"
        "┃┠─═❮    DATABASE    ❯═─⋆\n"
        "┃┴╭────────···\n"
        "┃┬╯\n"
        "┃╏  /logs\n"
        "┃╏  /delete\n"
        "┃╏  /deleteall\n"
        "┃┴╮\n"
        "┃┬╰────────···\n"
        "┃╰─────═┅═─────\n"
        "╰━━━━━━━━━━━━━◉"
    )

    # Create the inline keyboard with the cancel button
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="cancel")]])
    await message.reply_text(text, reply_markup=keyboard)


@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴀᴠᴀᴛᴀʀ: ᴛʜᴇ ᴡᴀʏ ᴏғ ᴡᴀᴛᴇʀ\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴍᴏɴᴇʏ ʜᴇɪsᴛ S01E01\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)")

def get_bot_version():
    # Replace with the code to fetch the bot version from wherever it's stored
    return "2.4.8"
    
    
# Start time of the bot
start_time = time.time()

# Function to get the bot runtime
def get_bot_runtime():
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time

# Example usage
runtime = get_bot_runtime()
print(f"Bot has been running for {runtime:.2f} seconds.")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pinging....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ\n{time_taken_s:.3f} ms")
    return time_taken_s
