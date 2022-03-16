from django.db import models


class PriceCard(models.Model):
    price = models.CharField(max_length=200, verbose_name='Цена')
    descript = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.descript

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    new_price = models.CharField(max_length=200, verbose_name='Новая цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
