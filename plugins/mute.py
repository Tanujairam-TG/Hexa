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
            "However, to access this, we kindly request that you ensure you have admin privileges within our group."
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
            "However, to access this, we kindly request that you ensure you have admin privileges within our group."
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
            "However, to access this, we kindly request that you ensure you have admin privileges within our group."
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

@Client.on_message(filters.command("purge") & filters.group & filters.me)
async def purge_messages(_, message):
    if len(message.command) != 2 or not message.command[1].isdigit():
        await message.reply_text("Usage: /purge <number of messages>")
        return

    count = int(message.command[1])
    messages = await message.client.get_chat_history(message.chat.id, limit=count + 1)
    for msg in messages:
        await msg.delete()

# Feature 4: Group Info
@Client.on_message(filters.command("groupinfo"))
async def group_info(_, message):
    chat = await message.client.get_chat(message.chat.id)
    members_count = await message.client.get_chat_members_count(message.chat.id)
    group_info_text = (
        f"Group Name: {chat.title}\n"
        f"Members Count: {members_count}"
    )
    await message.reply_text(group_info_text)
