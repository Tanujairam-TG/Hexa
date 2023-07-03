import datetime
import random
import time
import os
import requests
import json

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

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": support_group_id,
        "text": restart_message,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "😜 Click Me",
                        "callback_data": "sticker"
                    }
                ]
            ]
        }
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Failed to send restart message. Error: {response.text}")

# Handling callback queries
def handle_callback_query(callback_query):
    query_data = callback_query.get("data")
    if query_data == "sticker":
        sticker_url = "https://t.me/addstickers/tyan2d_anim"
        sticker_message = {
            "chat_id": callback_query["message"]["chat"]["id"],
            "sticker": sticker_url
        }
        response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendSticker", json=sticker_message)
        if response.status_code != 200:
            print(f"Failed to send sticker. Error: {response.text}")

# Delay before sending the restart message
time.sleep(5)  # Adjust the delay as needed

# Check restart flag and send message
if is_restarted:
    send_restart_message()
    
# Handling callback queries (example)
callback_query_data = {
    "message": {
        "chat": {
            "id": support_group_id
        }
    },
    "data": "sticker"
}
handle_callback_query(callback_query_data)
