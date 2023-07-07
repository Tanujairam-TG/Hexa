from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import ChatAdminRequired
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
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
            buttons = [
                [
                    InlineKeyboardButton('🚸 Support 🚸', url=f'https://t.me/+9Y0zeiIAFeczMDJl')
                ]
            ]
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
        buttons = [
            [
                InlineKeyboardButton('🤥 Help', url=f"https://t.me/{temp.U_NAME}?start=help"),
                InlineKeyboardButton('🔔 Updates', url='https://t.me/CinemaVenoOfficial')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=f"<b>Thank you for adding me to {message.chat.title} ❣️\n\nIf you have any questions or doubts about using me, contact support.</b>",
            reply_markup=reply_markup
        )
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
                    "welcome aboard!",
                ]
                custom_wish_string = "\n".join(f"├ ❖ Dear: {wish}" for wish in custom_wishes)

                temp.MELCOW['welcome'] = await message.reply(
                    f"┌─❖\n"
                    f"│ 「 Hi 」\n"
                    f"└┬❖\n"
                    f"┌┤❖  「{u.mention}」\n"
                    f"│└────────────┈ ⳹\n"
                    f"├❖ To {message.chat.title}!\n"
                    f"├ ❖ Enjoy your stay!\n"
                    f"{custom_wish_string}"
                    f"└────────────┈ ⳹",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎉 Support 🎉', url=f"https://t.me/{SUPPORT_CHAT}"),
                                InlineKeyboardButton('🚀 Updates', url=f"https://t.me/{LOG_CHANNEL.split('/')[1]}")
                            ]
                        ]
                    )
                )


@Client.on_message(filters.left_chat_member & filters.group)
async def goodbye(bot, message):
    settings = await get_settings(message.chat.id)
    if settings["goodbye"]:
        if temp.MELCOW.get('goodbye') is not None:
            try:
                await temp.MELCOW['goodbye'].delete()
            except:
                pass
        temp.MELCOW['goodbye'] = await message.reply(
            f"┌─❖\n"
            f"│ 「 Bye 」\n"
            f"└┬❖\n"
            f"┌┤❖  「{message.left_chat_member.mention}」\n"
            f"│└────────────┈ ⳹\n"
            f"├❖ Just left {message.chat.title}!\n"
            f"├ ❖ Hope to see you soon!\n"
            f"└────────────┈ ⳹",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🚑 Support 🚑', url=f"https://t.me/{SUPPORT_CHAT}"),
                        InlineKeyboardButton('🔔 Updates', url=f"https://t.me/{LOG_CHANNEL.split('/')[1]}")
                    ]
                ]
            )
        )


@Client.on_message(filters.command('setwelcome'))
async def set_welcome(_, message):
    if not message.from_user.id in ADMINS:
        return await message.reply(
            "❌ You are not allowed to access this command!"
        )

    if len(message.command) < 2:
        return await message.reply(
            "❌ Provide the welcome message to set!"
        )

    settings = await get_settings(message.chat.id)
    settings["welcome"] = True
    await db.set_settings(message.chat.id, settings)

    welcome_message = " ".join(message.command[1:])
    await message.reply_text(
        f"✅ Welcome message has been set successfully!\n\nNew Welcome Message:\n{welcome_message}"
    )


@Client.on_message(filters.command('setgoodbye'))
async def set_goodbye(_, message):
    if not message.from_user.id in ADMINS:
        return await message.reply(
            "❌ You are not allowed to access this command!"
        )

    if len(message.command) < 2:
        return await message.reply(
            "❌ Provide the goodbye message to set!"
        )

    settings = await get_settings(message.chat.id)
    settings["goodbye"] = True
    await db.set_settings(message.chat.id, settings)

    goodbye_message = " ".join(message.command[1:])
    await message.reply_text(
        f"✅ Goodbye message has been set successfully!\n\nNew Goodbye Message:\n{goodbye_message}"
    )

@Client.on_message(filters.command('welcome'))
async def welcome(bot, message):
    settings = await get_settings(message.chat.id)
    if settings["welcome"]:
        return await message.reply(
            "✅ Welcome messages are already enabled in this chat!"
        )

    settings["welcome"] = True
    await temp.SETTINGS.update_one({"chat_id": message.chat.id}, {"$set": settings})

    await message.reply_text(
        "✅ Welcome messages have been enabled successfully!"
    )


@Client.on_message(filters.command('goodbye'))
async def goodbye(bot, message):
    settings = await get_settings(message.chat.id)
    if settings["goodbye"]:
        return await message.reply(
            "✅ Goodbye messages are already enabled in this chat!"
        )

    settings["goodbye"] = True
    await temp.SETTINGS.update_one({"chat_id": message.chat.id}, {"$set": settings})

    await message.reply_text(
        "✅ Goodbye messages have been enabled successfully!"
    )


@Client.on_message(filters.command('nowelcome'))
async def nowelcome(bot, message):
    settings = await get_settings(message.chat.id)
    if not settings["welcome"]:
        return await message.reply(
            "✅ Welcome messages are already disabled in this chat!"
        )

    settings["welcome"] = False
    await temp.SETTINGS.update_one({"chat_id": message.chat.id}, {"$set": settings})

    await message.reply_text(
        "✅ Welcome messages have been disabled successfully!"
    )


@Client.on_message(filters.command('nogoodbye'))
async def nogoodbye(bot, message):
    settings = await get_settings(message.chat.id)
    if not settings["goodbye"]:
        return await message.reply(
            "✅ Goodbye messages are already disabled in this chat!"
        )

    settings["goodbye"] = False
    await temp.SETTINGS.update_one({"chat_id": message.chat.id}, {"$set": settings})

    await message.reply_text(
        "✅ Goodbye messages have been disabled successfully!"
    )


@Client.on_message(filters.command('delwelcome'))
async def delwelcome(bot, message):
    if not message.from_user.id in ADMINS:
        return await message.reply(
            "❌ You are not allowed to access this command!"
        )

    settings = await get_settings(message.chat.id)
    if not settings["welcome"]:
        return await message.reply(
            "✅ Welcome messages are already disabled in this chat!"
        )

    settings["welcome"] = False
    await temp.SETTINGS.update_one({"chat_id": message.chat.id}, {"$set": settings})

    await message.reply_text(
        "✅ Welcome messages have been disabled successfully!"
    )


@Client.on_message(filters.command('delgoodbye'))
async def delgoodbye(bot, message):
    if not message.from_user.id in ADMINS:
        return await message.reply(
            "❌ You are not allowed to access this command!"
        )

    settings = await get_settings(message.chat.id)
    if not settings["goodbye"]:
        return await message.reply(
            "✅ Goodbye messages are already disabled in this chat!"
        )

    settings["goodbye"] = False
    await temp.SETTINGS.update_one({"chat_id": message.chat.id}, {"$set": settings})

    await message.reply_text(
        "✅ Goodbye messages have been disabled successfully!"
    )


@Client.on_message(filters.command(["kick"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def kick(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    if reply_user_id == bot.get_me().id:
        await message.reply_text("I cannot kick myself!")
        return
    try:
        await bot.kick_chat_member(message.chat.id, reply_user_id)
        await message.reply_text("User kicked successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to kick users.")

@Client.on_message(filters.command(["ban"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def ban(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    if reply_user_id == bot.get_me().id:
        await message.reply_text("I cannot ban myself!")
        return
    try:
        await bot.kick_chat_member(message.chat.id, reply_user_id)
        await bot.unban_chat_member(message.chat.id, reply_user_id)
        await message.reply_text("User banned successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to ban users.")

@Client.on_message(filters.command(["unban"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def unban(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    try:
        await bot.unban_chat_member(message.chat.id, reply_user_id)
        await message.reply_text("User unbanned successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to unban users.")

@Client.on_message(filters.command(["pin"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def pin(_, message):
    reply_message_id = message.reply_to_message.message_id
    try:
        await bot.pin_chat_message(message.chat.id, reply_message_id)
        await message.reply_text("Message pinned successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to pin messages.")


@Client.on_message(filters.command(["unpin"]) & filters.group & filters.user(ADMINS))
async def unpin(_, message):
    try:
        await bot.unpin_chat_message(message.chat.id)
        await message.reply_text("Message unpinned successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to unpin messages.")

@Client.on_message(filters.command(["purge"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def purge(_, message):
    reply_message_id = message.reply_to_message.message_id
    try:
        await bot.delete_messages(message.chat.id, reply_message_id)
        await message.reply_text("Message deleted successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to delete messages.")

@Client.on_message(filters.command(["promote"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def promote(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    try:
        await bot.promote_chat_member(message.chat.id, reply_user_id)
        await message.reply_text("User promoted successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to promote users.")


@Client.on_message(filters.command(["demote"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def demote(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    try:
        await bot.promote_chat_member(
            chat_id=message.chat.id,
            user_id=reply_user_id,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False
        )
        await message.reply_text("User demoted successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to demote users.")


@Client.on_message(filters.command(["mute"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def mute(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    try:
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=reply_user_id,
            permissions=ChatPermissions(can_send_messages=False)
        )
        await message.reply_text("User muted successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to mute users.")


@Client.on_message(filters.command(["unmute"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def unmute(_, message):
    reply_user_id = message.reply_to_message.from_user.id
    try:
        await bot.restrict_chat_member(message.chat.id, reply_user_id, can_send_messages=True)
        await message.reply_text("User unmuted successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to unmute users.")

@Client.on_message(filters.command(["banall"]) & filters.group & filters.user(ADMINS))
async def banall(_, message):
    try:
        members = await bot.get_chat_members(message.chat.id)
        for member in members:
            user_id = member.user.id
            if user_id != bot.get_me().id:
                await bot.kick_chat_member(message.chat.id, user_id)
        await message.reply_text("All members banned successfully!")
    except ChatAdminRequired:
        await message.reply_text("I need administrative privileges to ban members.")

@Client.on_message(filters.command(["info"]) & filters.group & filters.user(ADMINS))
async def info(_, message):
    chat = message.chat
    members_count = await bot.get_chat_members_count(chat.id)
    text = f"Group Info:\n\nTitle: {chat.title}\nID: {chat.id}\nMembers: {members_count}"
    await message.reply_text(text)

@Client.on_message(filters.command(["id"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def id(bot, message):
    reply_user = message.reply_to_message.from_user
    text = f"User ID: {reply_user.id}\n\n{reply_user.mention}"
    await message.reply_text(text)

@Client.on_message(filters.command(["settings"]) & filters.group & filters.user(ADMINS))
async def settings(bot, message):
    settings = await get_settings(message.chat.id)
    welcome_status = "Enabled" if settings.get("welcome") else "Disabled"
    goodbye_status = "Enabled" if settings.get("goodbye") else "Disabled"
    welcome_text = settings.get("welcome_text", "Not set")
    goodbye_text = settings.get("goodbye_text", "Not set")
    text = f"Group Settings:\n\nWelcome: {welcome_status}\nWelcome Text: {welcome_text}\n\nGoodbye: {goodbye_status}\nGoodbye Text: {goodbye_text}"
    await message.reply_text(text)


@Client.on_message(filters.command(["setwelcome"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def setwelcome(bot, message):
    reply_text = message.reply_to_message.text
    if reply_text:
        settings = await get_settings(message.chat.id)
        settings["welcome_text"] = reply_text
        await db.set_settings(message.chat.id, settings)
        await message.reply_text("Welcome text set successfully!")
    else:
        await message.reply_text("Please reply to a message containing the welcome text.")

@Client.on_message(filters.command(["setgoodbye"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def setgoodbye(bot, message):
    reply_message = message.reply_to_message
    if reply_message and reply_message.text:
        reply_text = reply_message.text
        settings = await get_settings(message.chat.id)
        settings["goodbye_text"] = reply_text
        await db.set_settings(message.chat.id, settings)
        await message.reply_text("Goodbye text set successfully!")
    else:
        await message.reply_text("Please reply to a text message to set it as the goodbye text.")


@Client.on_message(filters.command(["enablewelcome"]) & filters.group & filters.user(ADMINS))
async def enablewelcome(bot, message):
    settings = await get_settings(message.chat.id)
    settings["welcome"] = True
    await db.set_settings(message.chat.id, settings)
    await message.reply_text("Welcome messages enabled!")

@Client.on_message(filters.command(["disablewelcome"]) & filters.group & filters.user(ADMINS))
async def disablewelcome(bot, message):
    settings = await get_settings(message.chat.id)
    settings["welcome"] = False
    await db.set_settings(message.chat.id, settings)
    await message.reply_text("Welcome messages disabled!")

@Client.on_message(filters.command(["enablegoodbye "]) & filters.group & filters.user(ADMINS))
async def enablegoodbye(bot, message):
    settings = await get_settings(message.chat.id)
    settings["goodbye"] = True
    await db.set_settings(message.chat.id, settings)
    await message.reply_text("Goodbye messages enabled!")

@Client.on_message(filters.command(["disablegoodbye"]) & filters.group & filters.user(ADMINS))
async def disablegoodbye(bot, message):
    settings = await get_settings(message.chat.id)
    settings["goodbye"] = False
    await db.set_settings(message.chat.id, settings)
    await message.reply_text("Goodbye messages disabled!")

@Client.on_message(filters.command(["cleanwelcome"]) & filters.group & filters.user(ADMINS))
async def cleanwelcome(bot, message):
    if (temp.MELCOW).get('welcome') is not None:
        try:
            await (temp.MELCOW['welcome']).delete()
            await message.reply_text("Welcome message cleaned!")
        except:
            pass
    else:
        await message.reply_text("There is no welcome message to clean.")

@Client.on_message(filters.command(["cleangoodbye"]) & filters.group & filters.user(ADMINS))
async def cleangoodbye(bot, message):
    if (temp.MELCOW).get('goodbye') is not None:
        try:
            await (temp.MELCOW['goodbye']).delete()
            await message.reply_text("Goodbye message cleaned!")
        except:
            pass
    else:
        await message.reply_text("There is no goodbye message to clean.")

@Client.on_message(filters.command(["filter"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def filter(bot, message):
    reply_message = message.reply_to_message
    if reply_message.media:
        media = Media(chat_id=message.chat.id, message_id=reply_message.message_id)
        await media.save()
        await message.reply_text("Message added to filtered media.")
    else:
        await message.reply_text("Please reply to a media message.")

@Client.on_message(filters.command(["unfilter"]) & filters.group & filters.user(ADMINS) & filters.reply)
async def unfilter(bot, message):
    reply_message_id = message.reply_to_message.message_id
    await Media.delete().where((Media.chat_id == message.chat.id) & (Media.message_id == reply_message_id)).gino.status()
    await message.reply_text("Message removed from filtered media.")

@Client.on_message(filters.command(["filtered"]) & filters.group & filters.user(ADMINS))
async def filtered(bot, message):
    filtered_media = await Media.query.where(Media.chat_id == message.chat.id).gino.all()
    if filtered_media:
        text = "Filtered Media:\n\n"
        for media in filtered_media:
            text += f"Message ID: {media.message_id}\n"
        await message.reply_text(text)
    else:
        await message.reply_text("There are no filtered media messages.")

@Client.on_message(filters.command(["cleanfiltered"]) & filters.group & filters.user(ADMINS))
async def cleanfiltered(bot, message):
    await Media.delete().where(Media.chat_id == message.chat.id).gino.status()
    await message.reply_text("Filtered media messages cleaned!")

@Client.on_message(filters.command(["help"]) & filters.group & filters.user(ADMINS))
async def help(bot, message):
    text = f"Hi, I'm the group management bot!\n\n"
    text += f"These are the available commands:\n\n"
    text += f"/kick - Kick a user\n"
    text += f"/ban - Ban a user\n"
    text += f"/unban - Unban a user\n"
    text += f"/pin - Pin a message\n"
    text += f"/unpin - Unpin the currently pinned message\n"
    text += f"/purge - Delete a message\n"
    text += f"/promote - Promote a user\n"
    text += f"/demote - Demote a user\n"
    text += f"/mute - Mute a user\n"
    text += f"/unmute - Unmute a user\n"
    text += f"/banall - Ban all members in the group\n"
    text += f"/info - Get group information\n"
    text += f"/id - Get the ID of a user\n"
    text += f"/settings - Get the group settings\n"
    text += f"/setwelcome - Set the welcome text\n"
    text += f"/setgoodbye - Set the goodbye text\n"
    text += f"/enablewelcome - Enable welcome messages\n"
    text += f"/disablewelcome - Disable welcome messages\n"
    text += f"/enablegoodbye - Enable goodbye messages\n"
    text += f"/disablegoodbye - Disable goodbye messages\n"
    text += f"/cleanwelcome - Clean the welcome message\n"
    text += f"/cleangoodbye - Clean the goodbye message\n"
    text += f"/filter - Add a message to filtered media\n"
    text += f"/unfilter - Remove a message from filtered media\n"
    text += f"/filtered - Get filtered media messages\n"
    text += f"/cleanfiltered - Clean filtered media messages\n"
    text += f"/help - Show this help message\n"
    await message.reply_text(text)

@Client.on_message(filters.command(["support"]) & filters.group & filters.user(ADMINS))
async def support(bot, message):
    await message.reply_text("For any queries or support, please contact the group admins.")
