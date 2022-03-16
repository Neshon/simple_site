import requests
from .models import TelegramSettings


def sendmessage(name, phone):
    settings = TelegramSettings.objects.get(pk=1)
    token = str(settings.token)
    chat_id = str(settings.chat_id)
    text = str(settings.msg + '\nИмя: ' + name + '\nНомер телефона: ' + phone)
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method,
                        data={'chat_id': chat_id,
                              'text': text})
