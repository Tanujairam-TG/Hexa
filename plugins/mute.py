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
            permissions=ChatPermissions(
            ),
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Be quiet for a while! 😠"
                f"{user_first_name}"
                f" muted for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "Be quiet for a while! 😠"
                f"<a href='tg://user?id={user_id}'>"
                "Of lavender"
                "</a>"
                " Mouth "
                f" muted for {message.command[1]}!"
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

@Client.on_message(filters.left_chat_member)
async def goodbye_message(_, message):
    goodbye_text = f"Goodbye, {message.from_user.first_name}! We'll miss you."
    await message.reply_text(goodbye_text)
