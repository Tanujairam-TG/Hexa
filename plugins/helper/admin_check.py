from pyrogram.types import Message, ChatMember
from pyrogram import filters, enums

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

    # Get information about the chat member (user)
    chat_member = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )

    # Check if the user is either the owner or an administrator of the chat
    return chat_member.status in [ChatMember.OWNER, ChatMember.ADMINISTRATOR]
