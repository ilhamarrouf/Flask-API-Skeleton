"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 02/05/20
    :time: 20.55
"""

import requests
import config
from app import app
from urllib.parse import urlencode


def telegram(message):
    if config.TELEGRAM_BOT_ENABLE:
        token = config.TELEGRAM_BOT_TOKEN
        chat_id = config.TELEGRAM_CHAT_ID

        message = '<b>' + config.APP_NAME + '</b> \n' \
            + '<b>' + config.ENV + '</b> \n' \
            + '<i>Message:</i> \n' \
            + '<code>' + message + '</code>'

        for id in chat_id.split('.'):
            try:
                requests.get('https://api.telegram.org/bot' + token + '/sendMessage', params=urlencode({
                    'text': message,
                    'chat_id': id,
                    'parse_mode': 'html',
                }))
            except Exception as err:
                app.logger.error(getattr(err, 'message', repr(err)))