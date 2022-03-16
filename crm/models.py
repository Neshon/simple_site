from django.db import models


class StatusCrm(models.Model):
    status = models.CharField(max_length=200, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    binding = models.ForeignKey(StatusCrm,
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Comment(models.Model):
    binding = models.ForeignKey(Order,
                                on_delete=models.CASCADE,
                                verbose_name='Заявка')
    text = models.TextField(verbose_name='Текст комментария')
    dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
