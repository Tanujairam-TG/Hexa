from pyrogram.types import Message
from pyrogram import Client, filters, enums

# Helper function to check for admin and owner privileges
async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return False

    if message.from_user.id in [
        777000,  # Telegram Service Notifications
        1087968824  # GroupAnonymousBot
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    
    admin_strings = [
        enums.ChatMemberStatus.CREATOR,
        enums.ChatMemberStatus.ADMINISTRATOR,
    ]
    
    if check_status.status not in admin_strings:
        return False
    else:
        return True
