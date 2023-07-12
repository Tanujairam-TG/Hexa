import datetime
import random
import string
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup

class User:
    def __init__(self, name):
        self.name = name
        self.muted = False
        self.mute_expiry = None
        self.unmute_time = None
        self.id = None
        self.authorization_code = None

class Group:
    def __init__(self):
        self.users = []
        self.admin_ids = set()

    def mute_user(self, user, duration_hours=None, duration_days=None):
        if user in self.users:
            user.muted = True
            if duration_hours is not None:
                mute_duration = datetime.timedelta(hours=duration_hours)
            elif duration_days is not None:
                mute_duration = datetime.timedelta(days=duration_days)
            else:
                mute_duration = None
            if mute_duration:
                user.mute_expiry = datetime.datetime.now() + mute_duration
                unmute_time = user.mute_expiry + datetime.timedelta(days=2)
                user.unmute_time = unmute_time
            else:
                user.mute_expiry = None
                user.unmute_time = None
            user.authorization_code = self.generate_authorization_code()

    def unmute_user(self, user):
        if user in self.users:
            user.muted = False
            user.mute_expiry = None
            user.unmute_time = None
            user.authorization_code = None

    def remove_message_permission(self, user_id):
        permissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_stickers=False,
            can_send_animations=False,
            can_send_games=False,
            can_use_inline_bots=False,
            can_add_web_page_previews=False,
            can_send_polls=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
        )
        return permissions

    def add_admin(self, user_id):
        self.admin_ids.add(user_id)

    def remove_admin(self, user_id):
        self.admin_ids.remove(user_id)

    def is_admin(self, user_id):
        return user_id in self.admin_ids

    def generate_authorization_code(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def send_message(self, user, message, authorization_code=None):
        if user in self.users:
            if user.muted and user.authorization_code != authorization_code:
                if datetime.datetime.now() < user.mute_expiry:
                    print(f"{user.name.mention} [{user.id}] is muted. Message not sent.")
                    return
                else:
                    self.unmute_user(user)

            print(f"{user.name.mention} [{user.id}]: {message}")


# Create Pyrogram client
app = Client("my_bot")

# Create groups
groups = {}

def create_group(group_id):
    group = Group()
    group.id = group_id
    group.users = []
    group.admin_ids = set()
    groups[group_id] = group
    return group

def get_group(group_id):
    return groups.get(group_id)

def add_group_admin(group_id, user_id):
    group = get_group(group_id)
    if group:
        group.add_admin(user_id)

def remove_group_admin(group_id, user_id):
    group = get_group(group_id)
    if group:
        group.remove_admin(user_id)

def mute_group_user(group_id, user_id, duration_hours=None, duration_days=None):
    group = get_group(group_id)
    if group:
        user = get_user(group, user_id)
        if user:
            group.mute_user(user, duration_hours, duration_days)

def remove_message_permission(group_id, user_id):
    group = get_group(group_id)
    if group:
        user = get_user(group, user_id)
        if user:
            return group.remove_message_permission(user_id)

def unmute_group_user(group_id, user_id):
    group = get_group(group_id)
    if group:
        user = get_user(group, user_id)
        if user:
            group.unmute_user(user)

def get_user(group, user_id):
    for user in group.users:
        if user.id == user_id:
            return user
    return None

# Register command handlers
@Client.on_message(filters.command(["mute"]))
def mute_command(client, message):
    group_id = message.chat.id
    user_id = message.from_user.id
    args = message.text.split()[1:]
    duration_hours = None
    duration_days = None
    for arg in args:
        if arg.endswith("h"):
            duration_hours = int(arg[:-1])
        elif arg.endswith("d"):
            duration_days = int(arg[:-1])
    mute_group_user(group_id, user_id, duration_hours, duration_days)
    if duration_hours is not None:
        message.reply_text(f"You have been muted for {duration_hours} hours.")
    elif duration_days is not None:
        message.reply_text(f"You have been muted for {duration_days} days.")
    else:
        message.reply_text("You have been muted permanently.")

@Client.on_message(filters.command(["unmute"]))
def unmute_command(client, message):
    group_id = message.chat.id
    user_id = message.from_user.id
    if is_group_admin(group_id, user_id):
        unmute_group_user(group_id, user_id)
        message.reply_text("You have been unmuted.")
    else:
        message.reply_text("Only admins can unmute users.")

@Client.on_callback_query()
def handle_button(client, callback_query):
    group_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    user = get_user(get_group(group_id), user_id)
    if user and user.muted:
        if is_group_admin(group_id, user_id):
            unmute_group_user(group_id, user_id)
            callback_query.answer("User has been unmuted.")
        else:
            callback_query.answer("Only admins can unmute the user.")

def is_group_admin(group_id, user_id):
    group = get_group(group_id)
    if group:
        return group.is_admin(user_id)
    return False

# Example usage
# Create group 1
group1 = create_group(123456789)
group1.users = [
    User("User1"),
    User("User2"),
    User("User3")
]
group1.add_admin(987654321)

# Create group 2
group2 = create_group(987654321)
group2.users = [
    User("User4"),
    User("User5"),
    User("User6")
]
group2.add_admin(123456789)

@app.on_message(filters.group)
def handle_group_message(client, message):
    group_id = message.chat.id
    user_id = message.from_user.id
    group = get_group(group_id)
    if group:
        user = get_user(group, user_id)
        if user and user.muted:
            if user.mute_expiry is None or datetime.datetime.now() < user.mute_expiry:
                permissions = remove_message_permission(group_id, user_id)
                if permissions:
                    client.restrict_chat_member(
                        chat_id=group_id,
                        user_id=user_id,
                        permissions=permissions,
                        until_date=user.unmute_time,
                    )
