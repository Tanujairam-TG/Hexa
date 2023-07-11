import datetime
import random
import string
import os
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import PeerIdInvalid
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Retrieve the bot token from the environment variable
TOKEN = os.environ.get('BOT_TOKEN')

# Create a dictionary to store group information
groups = {}

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.muted = False
        self.mute_expiry = None

class Group:
    def __init__(self, group_id):
        self.group_id = group_id
        self.users = []
        self.admin_ids = set()

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def add_admin(self, user_id):
        self.admin_ids.add(user_id)

    def remove_admin(self, user_id):
        self.admin_ids.remove(user_id)

    def is_admin(self, user_id):
        return user_id in self.admin_ids

    def mute_user(self, user_id, duration):
        user = self.get_user(user_id)
        if user:
            user.muted = True
            mute_expiry = datetime.datetime.now() + duration
            user.mute_expiry = mute_expiry
            permissions = ChatPermissions(can_send_messages=False)
            app.restrict_chat_member(self.group_id, user.user_id, permissions)
            app.send_message(
                self.group_id,
                f"{user.user_id} has been muted for {duration}.",
                reply_to_message_id=user_id
            )

    def unmute_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            user.muted = False
            user.mute_expiry = None
            permissions = ChatPermissions(can_send_messages=True)
            app.restrict_chat_member(self.group_id, user.user_id, permissions)
            app.send_message(
                self.group_id,
                f"{user.user_id} has been unmuted.",
                reply_to_message_id=user_id
            )

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

# Function to create a group
def create_group(group_id):
    group = Group(group_id)
    groups[group_id] = group
    return group

# Function to get a group by ID
def get_group(group_id):
    return groups.get(group_id)

# Function to add an admin to a group
def add_group_admin(group_id, user_id):
    group = get_group(group_id)
    if group:
        group.add_admin(user_id)

# Function to remove an admin from a group
def remove_group_admin(group_id, user_id):
    group = get_group(group_id)
    if group:
        group.remove_admin(user_id)

# Function to mute a user in a group
def mute_group_user(group_id, user_id, duration):
    group = get_group(group_id)
    if group:
        mute_duration = parse_duration(duration)
        if mute_duration:
            group.mute_user(user_id, mute_duration)
        else:
            app.send_message(
                group_id,
                "Invalid duration format. Please use 'X minutes', 'X hours', or 'X days'.",
                reply_to_message_id=user_id
            )

# Function to parse the mute duration string and return a timedelta object
def parse_duration(duration):
    duration = duration.lower().split()
    if len(duration) != 2:
        return None
    try:
        value = int(duration[0])
        unit = duration[1]
        if unit.endswith('s'):
            unit = unit[:-1]
        if unit == 'minute':
            return datetime.timedelta(minutes=value)
        elif unit == 'hour':
            return datetime.timedelta(hours=value)
        elif unit == 'day':
            return datetime.timedelta(days=value)
        else:
            return None
    except ValueError:
        return None

# Function to unmute a user in a group
def unmute_group_user(group_id, user_id):
    group = get_group(group_id)
    if group:
        group.unmute_user(user_id)

# Function to check if a user is an admin in the group
def is_group_admin(group_id, user_id):
    group = get_group(group_id)
    if group:
        return group.is_admin(user_id)
    return False

# Register command handlers
@Client.on_message(filters.command(["mute"]) & filters.group)
def mute_command(client, message):
    group_id = get_group_id(message.from_user.id)
    if not group_id:
        app.send_message(
            message.chat.id,
            "You are not connected to any group.",
            reply_to_message_id=message.message_id
        )
        return
    user_id = message.from_user.id
    duration = '60 minutes'  # Default duration if not specified in the command
    if len(message.command) > 1:
        duration = ' '.join(message.command[1:])
    mute_group_user(group_id, user_id, duration)

@Client.on_message(filters.command(["unmute"]) & filters.group)
def unmute_command(client, message):
    group_id = get_group_id(message.from_user.id)
    if not group_id:
        app.send_message(
            message.chat.id,
            "You are not connected to any group.",
            reply_to_message_id=message.message_id
        )
        return
    user_id = message.from_user.id
    if is_group_admin(group_id, user_id):
        unmute_group_user(group_id, user_id)
    else:
        app.send_message(
            group_id,
            "Only admins can unmute users.",
            reply_to_message_id=message.message_id
        )

# Function to get the group ID from the connection
def get_group_id(user_id):
    connections = all_connections(str(user_id))
    if connections:
        connection = connections[0]  # Assuming there is only one connection
        return connection['group_id']
    return None

# Function to get the connections for a user
def get_connections(user_id):
    return all_connections(str(user_id))

# Get connections for a specific user
user_id = 123456789
connections = get_connections(user_id)

# Iterate over the connections and add them to the groups dictionary
for connection in connections:
    group_id = connection['group_id']
    group = create_group(group_id)
    group.add_admin(user_id)
    # Add other information to the group if needed
