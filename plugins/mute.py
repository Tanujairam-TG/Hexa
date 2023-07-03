import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ParseMode

# Telegram bot setup
bot_token = os.environ.get("BOT_TOKEN")

# Dictionary to keep track of muted users
muted_users = {}

# Mute a user from sending messages
def mute_user(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.message.reply_to_message.from_user.id
    user_mention = update.message.reply_to_message.from_user.mention_markdown_v2()

    # Add the user to the muted_users dictionary
    muted_users[chat_id] = user_id

    update.message.reply_text(f"User {user_mention} has been muted.")

# Unmute a user
def unmute_user(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.message.reply_to_message.from_user.id
    user_mention = update.message.reply_to_message.from_user.mention_markdown_v2()

    if chat_id in muted_users and muted_users[chat_id] == user_id:
        del muted_users[chat_id]
        update.message.reply_text(f"User {user_mention} has been unmuted.")
    else:
        update.message.reply_text("No user is currently muted.")

# Check if a user is muted
def is_user_muted(chat_id, user_id):
    return chat_id in muted_users and muted_users[chat_id] == user_id

# Handle incoming messages
def handle_message(update: Update, context):
    chat_id = update.effective_chat.id
    user_id = update.message.from_user.id

    if is_user_muted(chat_id, user_id):
        update.message.delete()
        user_mention = update.message.from_user.mention_markdown_v2()
        update.message.reply_text(f"{user_mention}, you are currently muted and cannot send messages.")

# Create the Telegram bot and set up handlers
updater = Updater(bot_token)
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler("mute", mute_user))
dispatcher.add_handler(CommandHandler("unmute", unmute_user))

# Add message handler
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
