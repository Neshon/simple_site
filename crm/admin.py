from django.contrib import admin
from .models import Order, StatusCrm, Comment


admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(Comment)
