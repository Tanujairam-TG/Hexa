import datetime
import random
import string
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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

    def mute_user(self, user, duration_minutes):
        if user in self.users:
            user.muted = True
            mute_duration = datetime.timedelta(minutes=duration_minutes)
            user.mute_expiry = datetime.datetime.now() + mute_duration
            unmute_time = user.mute_expiry + datetime.timedelta(days=2)
            user.unmute_time = unmute_time
            user.authorization_code = self.generate_authorization_code()

    def unmute_user(self, user):
        if user in self.users:
            user.muted = False
            user.mute_expiry = None
            user.unmute_time = None
            user.authorization_code = None

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
                    print(f"{user.name} [{user.id}] is muted. Message not sent.")
                    return
                else:
                    self.unmute_user(user)

            print(f"{user.name} [{user.id}]: {message}")

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

def mute_group_user(group_id, user_id, duration_minutes):
    group = get_group(group_id)
    if group:
        user = get_user(group, user_id)
        if user:
            group.mute_user(user, duration_minutes)

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
    duration_minutes = 60
    mute_group_user(group_id, user_id, duration_minutes)
    message.reply_text("You have been muted for 60 minutes.")

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
