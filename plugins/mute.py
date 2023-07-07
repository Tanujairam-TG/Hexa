import osimport osimport os
from telegram import ChatPermissions
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

# Handler function to process the mute command
def mute_user(update, context):
    # Get the user ID of the user to be muted
    user_id = update.message.reply_to_message.from_user.id
    
    # Get the mute duration from the command parameter
    duration_param = context.args[0]
    duration = parse_duration(duration_param)
    
    # Calculate the mute until_date
    until_date = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    
    # Mute the user in the group for the specified duration
    context.bot.restrict_chat_member(
        chat_id=update.effective_chat.id,
        user_id=user_id,
        permissions=ChatPermissions(can_send_messages=False),
        until_date=until_date
    )
    
    # Send a confirmation message
    update.message.reply_text(f"User {user_id} has been muted for {duration_param}.")

# Function to parse the mute duration parameter
def parse_duration(duration_param):
    duration_param = duration_param.lower()
    if duration_param.endswith("h"):
        hours = int(duration_param[:-1])
        return hours * 60 * 60
    elif duration_param.endswith("d"):
        days = int(duration_param[:-1])
        return days * 24 * 60 * 60
    else:
        raise ValueError("Invalid duration parameter. Please specify the duration in hours (h) or days (d).")

# Get the bot token from environment variable
bot_token = os.environ.get("BOT_TOKEN")

# Create an instance of the Updater using the bot token
updater = Updater(token=bot_token, use_context=True)

# Register the mute command handler
updater.dispatcher.add_handler(CommandHandler('mute', mute_user))

