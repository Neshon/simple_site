from django.contrib import admin
from .models import Order, StatusCrm, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment
    fields = ('dt', 'text')
    readonly_fields = ('dt',)
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_dt', 'order_name', 'order_phone', 'binding')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_dt', 'order_name', 'order_phone')
    list_filter = ('binding',)
    list_editable = ('binding', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_dt', 'order_name', 'order_phone', 'binding')
    readonly_fields = ('id', 'order_dt')
    inlines = [CommentAdmin, ]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(Comment)
