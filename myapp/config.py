import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN', 'devtoken')
    ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN', 'your_temp_token')
    PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID', 'your_number_id')
