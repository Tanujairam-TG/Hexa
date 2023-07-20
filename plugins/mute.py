from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from plugins.helper.admin_check import admin_check
from plugins.helper.extract import extract_time, extract_user                               


@Client.on_message(filters.command("mute"))
async def mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "To access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions()
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        await message.reply_text(
            f"👍🏻 {user_first_name}'s mouth is shut! 🤐"
        )


@Client.on_message(filters.command("tmute"))
async def temp_mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "To access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time type specified. "
                "Expected m, h, or d, Got it: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(),
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        await message.reply_text(
            f"Be quiet for a while! 😠 {user_first_name} muted for {message.command[1]}!"
        )


@Client.on_message(filters.command("unmute"))
async def unmute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "To access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"🎉 {user_first_name} is free to speak now! 🗣️"
        )


@Client.on_message(filters.command("promote"))
async def promote_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "To access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.promote_member(user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"✨ {user_first_name} has been promoted to an admin! 🎉"
        )


@Client.on_message(filters.command("demote"))
async def demote_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(
            "Attention: Admin Privileges Required\n\n"
            "Dear member,\n\n"
            "To access this, we kindly request that you ensure you have admin privileges within our group."
        )
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"🔥 {user_first_name} has been demoted to a regular member!"
        )

@Client.on_message(filters.command("purge"))
async def purge_messages(_, message):
    if not message.reply_to_message:
        await message.reply_text("Please reply to the message you want to purge.")
        return

    message_id = message.reply_to_message.message_id
    chat_id = message.chat.id

    try:
        await Client.delete_messages(chat_id, message_id)
        await message.reply_text("Message purged.")
    except Exception as e:
        await message.reply_text("Failed to purge the message.")

@Client.on_chat_member_leave()
async def farewell_member(_, message):
    left_member_name = message.left_chat_member.first_name
    farewell_message = f"Goodbye, {left_member_name}! We'll miss you!"
    await message.reply_text(farewell_message)

@Client.on_message(filters.command("kick"))
async def kick_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text("You must be an admin to use this command.")
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.kick_member(user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(f"{user_first_name} has been kicked from the group.")
