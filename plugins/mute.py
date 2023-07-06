import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Retrieve the bot token from the environment
TOKEN = os.environ.get('BOT_TOKEN')

# Create an Updater object
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the command handler function for /mute
def mute(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user_id = update.message.reply_to_message.from_user.id
    context.bot.restrict_chat_member(chat_id, user_id, can_send_messages=False)

# Define the command handler function for /unmute
def unmute(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user_id = update.message.reply_to_message.from_user.id
    context.bot.restrict_chat_member(chat_id, user_id, can_send_messages=True)

# Add the command handlers to the dispatcher
dispatcher.add_handler(CommandHandler("mute", mute))
dispatcher.add_handler(CommandHandler("unmute", unmute))

# Start the bot
updater.start_polling()
