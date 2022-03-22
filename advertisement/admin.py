from django.contrib import admin
from .models import Advertisement, Author, Category, AdvertisementStatus


admin.site.register(Advertisement)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(AdvertisementStatus)
