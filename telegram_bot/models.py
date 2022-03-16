from django.db import models


class TelegramSettings(models.Model):
    token = models.CharField(max_length=200, verbose_name='Токен')
    chat_id = models.CharField(max_length=200, verbose_name='ID')
    msg = models.TextField(verbose_name='Текст сообщений')

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
