import requests
from .models import TelegramSettings


def sendmessage(name, phone):
    if TelegramSettings.objects.get(pk=1):
        settings = TelegramSettings.objects.get(pk=1)
        token = str(settings.token)
        chat_id = str(settings.chat_id)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        text = str(settings.msg + '\nИмя: ' + name + '\nНомер телефона: ' + phone)

        try:
            req = requests.post(method,
                                data={'chat_id': chat_id,
                                      'text': text})
        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё хорошо. Сообщение отправлено!')
    else:
        pass
