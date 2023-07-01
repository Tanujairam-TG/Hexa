import time
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

    ping_value = await ping(_, message)

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
                "└┬❖\n"
                 f"│✑ 𝙃𝙚𝙡𝙡𝙤, {message.from_user.first_name}\n"
                 f"│✑ 𝙈𝙮𝙨𝙚𝙡𝙛:- 📍 <a href=https://t.me/Hexa_md_BOT>Ｈｅｘａ</a>\n"
                 f"│✑ 𝙑𝙚𝙧𝙨𝙞𝙤𝙣:- ♻️{get_bot_version()}\n"
                 f"│✑ 𝘼 𝙗𝙤𝙩 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮:- <a href=https://t.me/CinemaVenoOfficial>ᶜᵛᵒ</a>\n"
                 f"│✑ 𝘽𝙤𝙩 𝙍𝙪𝙣𝙩𝙞𝙢𝙚:- 🛰️{elapsed_time_formatted}\n"
                 "└───────────────┈ ⳹",
        reply_markup=keyboard
    )




    
@Client.on_message(filters.
command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Fᴏʀ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@Client.on_message(filters.command("movies", CMD))
async def movie(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴀᴠᴀᴛᴀʀ: ᴛʜᴇ ᴡᴀʏ ᴏғ ᴡᴀᴛᴇʀ\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\nꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\nɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ\n\nᴇxᴀᴍᴘʟᴇ : ᴍᴏɴᴇʏ ʜᴇɪsᴛ S01E01\n\n🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)")

def get_bot_version():
    # Replace with the code to fetch the bot version from wherever it's stored
    return "2.4.3"
    
    
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
