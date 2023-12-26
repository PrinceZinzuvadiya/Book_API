from django.contrib import admin
from .models import books

class bookadmin(admin.ModelAdmin):
    list_display=['title', 'author', 'lsbn', 'publisher']
admin.site.register(books, bookadmin)
