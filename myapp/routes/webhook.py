from flask import Blueprint, request, current_app
from myapp.services.whatsapp import process_message

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == current_app.config['VERIFY_TOKEN']:
            return request.args.get('hub.challenge')
        return "Verification failed", 403

    data = request.get_json()
    process_message(data)
    return "ok", 200
