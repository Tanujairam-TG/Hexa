from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import ChatAdminRequired
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script

"""-----------------------------------------https://t.me/CinemaVenoOfficial --------------------------------------"""

@Client.on_message(filters.new_chat_members & filters.group)
async def save_group(bot, message):
    r_j_check = [u.id for u in message.new_chat_members]
    if temp.ME in r_j_check:
        if not await db.get_chat(message.chat.id):
            total = await bot.get_chat_members_count(message.chat.id)
            r_j = message.from_user.mention if message.from_user else "Anonymous" 
            await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, r_j))       
            await db.add_chat(message.chat.id, message.chat.title)
        if message.chat.id in temp.BANNED_CHATS:
            # Inspired from a boat of a banana tree
            buttons = [[
                InlineKeyboardButton('🚸 Support 🚸', url=f'https://t.me/+9Y0zeiIAFeczMDJl')
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            k = await message.reply(
                text='<b>CHAT NOT ALLOWED 🐞\n\nMy admins have restricted me from working here! If you want to know more about it, contact support.</b>',
                reply_markup=reply_markup,
            )

            try:
                await k.pin()
            except:
                pass
            await bot.leave_chat(message.chat.id)
            return
        buttons = [[
            InlineKeyboardButton('🤥 Help', url=f"https://t.me/{temp.U_NAME}?start=help"),
            InlineKeyboardButton('🔔 Updates', url='https://t.me/CinemaVenoOfficial')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>Thank you for adding me to {message.chat.title} ❣️\n\nIf you have any questions or doubts about using me, contact support.</b>",
            reply_markup=reply_markup)
    else:
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            for u in message.new_chat_members:
                if temp.MELCOW.get('welcome') is not None:
                    try:
                        await temp.MELCOW['welcome'].delete()
                    except:
                        pass
                custom_wishes = [
                    "Have a great time!",
                ]
                custom_wish_string = ""
                for wish in custom_wishes:
                    custom_wish_string += f"│✑ Custom Wish: {wish}\n"

                temp.MELCOW['welcome'] = await message.reply(
                    "┌─❖\n"
                f"│ 「 Hi 」\n"
                f"└┬❖\n"
                f"┌┤✑ Welcome,「{u.mention}!」\n"
                f"│└────────────┈ ⳹\n"
                f"│✑ To {message.chat.title}!\n"
                f"│✑ Enjoy your stay!\n"
                f"│✑ Role: Member\n"
                f"├❖ Contact for any queries!\n"
                "└───────────────┈ ⳹",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🤥 Help', url=f"https://t.me/{temp.U_NAME}?start=help")], [InlineKeyboardButton('🔔 Updates', url='https://t.me/CinemaVenoOfficial')]]))

@Client.on_message(filters.left_chat_member & filters.group)
async def goodbye(bot, message):
    settings = await get_settings(message.chat.id)
    if settings["goodbye"]:
        for user in message.left_chat_member:
            if temp.MELCOW.get('goodbye') is not None:
                try:
                    await temp.MELCOW['goodbye'].delete()
                except:
                    pass
            temp.MELCOW['goodbye'] = await message.reply(
                f"┌─❖\n"
                f"│ 「 Bye 」\n"
                f"└┬❖\n"
                f"│✑ Goodbye, {user.mention}!\n"
                f"└─❖\n",
                reply_to_message_id=message.message_id
            )

@Client.on_message(filters.command("settings") & filters.private & filters.user(ADMINS))
async def settings(bot, message):
    chat_id = message.chat.id
    settings = await get_settings(chat_id)
    text = f"<b>Settings for Chat ID: {chat_id}</b>\n\n"
    text += f"Welcome: <b>{settings['welcome']}</b>\n"
    text += f"Goodbye: <b>{settings['goodbye']}</b>\n"
    await message.reply_text(text)

@Client.on_message(filters.command("setwel") & filters.private & filters.user(ADMINS))
async def setwel(bot, message):
    chat_id = message.chat.id
    try:
        val = message.command[1].lower()
    except IndexError:
        await message.reply_text("Please provide a value (on/off) for welcome.")
        return
    if val in ("on", "off"):
        await db.set_welcome(chat_id, val == "on")
        await message.reply_text(f"Welcome message has been turned {val} successfully.")
    else:
        await message.reply_text("Invalid value! Please provide either 'on' or 'off'.")

@Client.on_message(filters.command("setbye") & filters.private & filters.user(ADMINS))
async def setbye(bot, message):
    chat_id = message.chat.id
    try:
        val = message.command[1].lower()
    except IndexError:
        await message.reply_text("Please provide a value (on/off) for goodbye.")
        return
    if val in ("on", "off"):
        await db.set_goodbye(chat_id, val == "on")
        await message.reply_text(f"Goodbye message has been turned {val} successfully.")
    else:
        await message.reply_text("Invalid value! Please provide either 'on' or 'off'.")

@Client.on_message(filters.command("pin") & filters.private & filters.user(ADMINS))
async def pin(bot, message):
    chat_id = message.chat.id
    try:
        msg_id = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid message ID.")
        return

    try:
        await bot.pin_chat_message(chat_id, msg_id)
        await message.reply_text("Message pinned successfully.")
    except Exception as e:
        await message.reply_text(f"An error occurred while pinning the message:\n\n{str(e)}")

@Client.on_message(filters.command("unpin") & filters.private & filters.user(ADMINS))
async def unpin(bot, message):
    chat_id = message.chat.id

    try:
        await bot.unpin_chat_message(chat_id)
        await message.reply_text("Message unpinned successfully.")
    except Exception as e:
        await message.reply_text(f"An error occurred while unpinning the message:\n\n{str(e)}")

@Client.on_message(filters.command("broadcast") & filters.private & filters.user(ADMINS))
async def broadcast(bot, message):
    try:
        text = message.text.split("/broadcast ", maxsplit=1)[1]
    except IndexError:
        await message.reply_text("Please provide the text to broadcast.")
        return

    chats = await db.get_all_chats()
    for chat_id in chats:
        try:
            await bot.send_message(chat_id, text)
        except ChatAdminRequired:
            await db.remove_chat(chat_id)

    await message.reply_text("Broadcast sent successfully.")

@Client.on_callback_query()
async def button(bot, callback_query):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    if callback_query.data == "yes":
        await callback_query.message.delete()
        try:
            await bot.leave_chat(chat_id)
        except:
            pass
        await db.remove_chat(chat_id)
        await bot.send_message(LOG_CHANNEL, script.LOG_TEXT_L.format(chat_id, message_id))

@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMINS))
async def stats(bot, message):
    total_chats = await db.get_total_chats()
    total_users = await db.get_total_users()
    total_media = await Media.count()
    total_size = await get_size()
    await message.reply_text(
        f"<b>Stats:</b>\n\n"
        f"Total Chats: {total_chats}\n"
        f"Total Users: {total_users}\n"
        f"Total Media: {total_media}\n"
        f"Total Size: {total_size}",
        parse_mode="html"
    )
