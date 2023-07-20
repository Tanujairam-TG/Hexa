from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from plugins.helper.admin_check import admin_check
from plugins.helper.extract import extract_time, extract_user


def not_admin_message():
    return (
        "Attention: Admin Privileges Required\n\n"
        "Dear members,\n\n"
        "We are thrilled to announce that we have a special treat in store for you! "
        "However, to access this, we kindly request that you ensure you have admin privileges within our group."
    )


def no_permission_message():
    return "You have no permission to perform this action. Contact the group owner."


@Client.on_message(filters.command("mute"))
async def mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(not_admin_message())
        return

    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions()
        )
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"🤐 Muted {user_first_name}'s mouth. Shhh! 🤫"
        )


@Client.on_message(filters.command("tmute"))
async def temp_mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(not_admin_message())
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
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"😡 Temporarily muted {user_first_name} for {message.command[1]}! 😠"
        )


@Client.on_message(filters.command("unmute"))
async def unmute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(not_admin_message())
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"🎉 Unmuted {user_first_name}. They can speak again! 🗣️"
        )


@Client.on_message(filters.command("promote"))
async def promote_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(not_admin_message())
        return

    if not message.from_user.is_chat_owner():
        await message.reply_text(no_permission_message())
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.promote_member(user_id)
    except Exception as error:
        if "not enough rights to restrict/unrestrict chat members" in str(error):
            await message.reply_text(no_permission_message())
        else:
            await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"👑 Promoted {user_first_name} to admin! 🎉"
        )


@Client.on_message(filters.command("demote"))
async def demote_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        await message.reply_text(not_admin_message())
        return

    if not message.from_user.is_chat_owner():
        await message.reply_text(no_permission_message())
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False
            )
        )
    except Exception as error:
        if "not enough rights to restrict/unrestrict chat members" in str(error):
            await message.reply_text(no_permission_message())
        else:
            await message.reply_text(str(error))
    else:
        await message.reply_text(
            f"🔇 Demoted {user_first_name} from admin! 😔"
        )
