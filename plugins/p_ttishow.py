from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

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
        if (temp.MELCOW).get('welcome') is not None:
            welcome_text = temp.MELCOW['welcome']
            await message.reply_text(
                text=welcome_text,
                reply_markup=reply_markup,
            )
            (temp.MELCOW['welcome']).delete()
        else:
            try:
                text = script.NEW_CHAT_MEMBER_G.format(message.chat.title, message.chat.id, message.chat.username,
                                                       message.from_user.id, message.from_user.mention)
                await message.reply_text(
                    text=text,
                    reply_markup=reply_markup,
                )
            except MessageTooLong:
                try:
                    await message.reply_text(
                        text=script.NEW_CHAT_MEMBER_G.format(message.chat.title, message.chat.id,
                                                             message.chat.username),
                        reply_markup=reply_markup,
                    )
                except MessageTooLong:
                    pass


@Client.on_message(filters.left_chat_member & filters.group)
async def goodbye(bot, message):
    if (temp.MELCOW).get('goodbye') is not None:
        goodbye_text = temp.MELCOW['goodbye']
        await message.reply_text(
            text=goodbye_text,
        )
        (temp.MELCOW['goodbye']).delete()
    else:
        try:
            text = script.LEFT_CHAT_MEMBER_G.format(message.chat.title, message.chat.id, message.chat.username,
                                                    message.from_user.id, message.from_user.mention)
            await message.reply_text(text=text)
        except MessageTooLong:
            try:
                await message.reply_text(
                    text=script.LEFT_CHAT_MEMBER_G.format(message.chat.title, message.chat.id, message.chat.username),
                )
            except MessageTooLong:
                pass


# group info

@Client.on_message(filters.command("group_info") & filters.group & filters.user(ADMINS))
async def group_info(client, message):
    chat = message.chat
    chat_id = chat.id
    total = await client.get_chat_members_count(chat_id)
    link = await client.export_chat_invite_link(chat_id)
    text = script.GROUP_INFO_TEXT.format(chat.title, chat_id, total, link)
    await message.reply_text(text)


# welcome message settings

@Client.on_message(filters.command("get_welcome") & filters.group & filters.user(ADMINS))
async def get_group_settings(client, message):
    if 'welcome' in temp.MELCOW:
        await message.reply_text(temp.MELCOW['welcome'])
    else:
        await message.reply_text("Welcome message is not set.")


@Client.on_message(filters.command("enable_welcome") & filters.group & filters.user(ADMINS))
async def enable_welcome_message(client, message):
    if 'welcome' in temp.MELCOW:
        await message.reply_text("Welcome message is already enabled.")
    else:
        temp.MELCOW['welcome'] = "Welcome to the group!"
        await message.reply_text("Welcome message has been enabled.")


@Client.on_message(filters.command("disable_welcome") & filters.group & filters.user(ADMINS))
async def disable_welcome_message(client, message):
    if 'welcome' in temp.MELCOW:
        del temp.MELCOW['welcome']
        await message.reply_text("Welcome message has been disabled.")
    else:
        await message.reply_text("Welcome message is already disabled.")


@Client.on_message(filters.command("set_welcome") & filters.group & filters.user(ADMINS))
async def set_welcome_text(client, message):
    if len(message.command) > 1:
        welcome_text = " ".join(message.command[1:])
        temp.MELCOW['welcome'] = welcome_text
        await message.reply_text("Welcome message has been set.")
    else:
        await message.reply_text("Please provide the welcome message.")


# goodbye message settings

@Client.on_message(filters.command("get_goodbye") & filters.group & filters.user(ADMINS))
async def get_goodbye_settings(client, message):
    if 'goodbye' in temp.MELCOW:
        await message.reply_text(temp.MELCOW['goodbye'])
    else:
        await message.reply_text("Goodbye message is not set.")


@Client.on_message(filters.command("enable_goodbye") & filters.group & filters.user(ADMINS))
async def enable_goodbye_message(client, message):
    if 'goodbye' in temp.MELCOW:
        await message.reply_text("Goodbye message is already enabled.")
    else:
        temp.MELCOW['goodbye'] = "Goodbye! Hope to see you again."
        await message.reply_text("Goodbye message has been enabled.")


@Client.on_message(filters.command("disable_goodbye") & filters.group & filters.user(ADMINS))
async def disable_goodbye_message(client, message):
    if 'goodbye' in temp.MELCOW:
        del temp.MELCOW['goodbye']
        await message.reply_text("Goodbye message has been disabled.")
    else:
        await message.reply_text("Goodbye message is already disabled.")


@Client.on_message(filters.command("set_goodbye") & filters.group & filters.user(ADMINS))
async def set_goodbye_text(client, message):
    if len(message.command) > 1:
        goodbye_text = " ".join(message.command[1:])
        temp.MELCOW['goodbye'] = goodbye_text
        await message.reply_text("Goodbye message has been set.")
    else:
        await message.reply_text("Please provide the goodbye message.")
