def get_auto_reply(text):
    text = text.lower()
    if "service" in text:
        return "We offer chatbot development, automation, and more."
    elif "support" in text:
        return "You can reach support at support@example.com"
    elif "office" in text:
        return "We're located in Ibadan, Nigeria."
    else:
        return "Sorry, I didn't get that. Type 'services', 'support', or 'office'."
