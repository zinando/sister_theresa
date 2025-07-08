import requests
from flask import current_app
from myapp.utils.parser import get_auto_reply

def send_whatsapp_message(to, text):
    url = f"https://graph.facebook.com/v19.0/{current_app.config['PHONE_NUMBER_ID']}/messages"
    headers = {
        "Authorization": f"Bearer {current_app.config['ACCESS_TOKEN']}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def process_message(data):
    if data.get("entry"):
        for entry in data["entry"]:
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                for message in messages:
                    user_text = message["text"]["body"]
                    sender_id = message["from"]
                    reply = get_auto_reply(user_text)
                    send_whatsapp_message(sender_id, reply)
