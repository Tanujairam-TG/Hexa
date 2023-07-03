import datetime
import random
import time
import os
import requests

# Generating a random restart time between 2 and 16 minutes, and 0 to 59 seconds
restart_time_minutes = random.randint(2, 16)
restart_time_seconds = random.randint(0, 59)
restart_time = datetime.timedelta(minutes=restart_time_minutes, seconds=restart_time_seconds)

# Telegram bot setup
bot_token = os.environ.get("BOT_TOKEN")
support_group_id = os.environ.get("SUPPORT_CHANNEL")

# Restart flag
is_restarted = True

# Sending the restart message to the support group
def send_restart_message():
    restart_message = "⚡ Bot Restarted ⚡\n"
    restart_message += f"🥂 Time Taken: {restart_time_minutes} Minutes {restart_time_seconds} Seconds"

    sticker_url = "https://t.me/addstickers/tyan2d_anim"
    sticker_data = {
        "chat_id": support_group_id,
        "sticker": sticker_url
    }
    sticker_response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendSticker", json=sticker_data)
    if sticker_response.status_code != 200:
        print(f"Failed to send sticker. Error: {sticker_response.text}")

    message_data = {
        "chat_id": support_group_id,
        "text": restart_message
    }
    message_response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", json=message_data)
    if message_response.status_code != 200:
        print(f"Failed to send restart message. Error: {message_response.text}")

# Delay before sending the restart message
time.sleep(5)  # Adjust the delay as needed

# Check restart flag and send message
if is_restarted:
    send_restart_message()
