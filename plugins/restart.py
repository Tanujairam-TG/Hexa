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
                [{"text": "🦋", "callback_data": "alive"}]
            ]
        }
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Failed to send restart message. Error: {response.text}")

# Handling the callback query from the button
def handle_callback_query(callback_query):
    query_id = callback_query["id"]
    chat_id = callback_query["message"]["chat"]["id"]
    data = callback_query["data"]
    
    if data == "alive":
        send_reply_message(chat_id)
        answer_callback_query(query_id, "Button clicked!")

# Sending the reply message when the button is clicked
def send_reply_message(chat_id):
    reply_message = "I'm alive! 🦄"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": reply_message
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Failed to send reply message. Error: {response.text}")

# Sending the answer for the callback query
def answer_callback_query(query_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/answerCallbackQuery"
    data = {
        "callback_query_id": query_id,
        "text": text
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Failed to answer callback query. Error: {response.text}")

# Delay before sending the restart message
time.sleep(5)  # Adjust the delay as needed

# Check restart flag and send message
if is_restarted:
    send_restart_message()
