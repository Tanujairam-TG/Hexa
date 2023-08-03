import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Admin user IDs from environment variable
admin_user_ids = os.environ.get("ADMINS", "").split(",")

# Koyeb API token
koyeb_api_token = os.environ.get("KOYEB_API_TOKEN")

# Koyeb service ID
koyeb_service_id = os.environ.get("KOYEB_SERVICE_ID")

# Telegram bot token
bot_token = os.environ.get("BOT_TOKEN")

@app.route(f'/{bot_token}', methods=['POST'])
def handle_update_command():
    data = request.json
    
    # Extract information from the incoming message
    if "message" in data and "text" in data["message"]:
        message_text = data["message"]["text"]
        chat_id = data["message"]["chat"]["id"]
        user_id = data["message"]["from"]["id"]
        
        # Check if the user is an admin
        if str(user_id) in admin_user_ids:
            if message_text.strip().lower() == "/update":
                # Trigger redeployment of the Koyeb service
                url = f"https://api.koyeb.com/v1/services/{koyeb_service_id}/redeploy"
                headers = {
                    "Authorization": f"Bearer {koyeb_api_token}"
                }
                response = requests.post(url, headers=headers)
                
                if response.status_code == 200:
                    response_text = "Service redeployment triggered successfully!"
                    
                    # Send completion message to the user
                    send_completion_message(chat_id)
                else:
                    response_text = "Failed to trigger service redeployment."
            else:
                response_text = "Unknown command."
        else:
            response_text = "You are not authorized to use this command."
        
        # Send response back to Telegram
        response_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response_data = {
            "chat_id": chat_id,
            "text": response_text
        }
        response = requests.post(response_url, json=response_data)
    
    return "OK"

def send_completion_message(chat_id):
    completion_message = "Service redeployment completed!"
    response_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response_data = {
        "chat_id": chat_id,
        "text": completion_message
    }
    response = requests.post(response_url, json=response_data)
    
