from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200,
                             db_index=True,
                             verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    views_count = models.IntegerField(default=0,
                                      verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата изменения')
    ended_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата окончания')
    status = models.ForeignKey('AdvertisementStatus',
                               default=None,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='advertisements',
                               verbose_name='Статус')
    author = models.ForeignKey('Author',
                               related_name='advertisements',
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    category = models.ForeignKey('Category',
                                 related_name='advertisements',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя статуса')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.IntegerField(verbose_name='Телефон')

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=200, verbose_name='Наименование')

    def __str__(self):
        return self.category
