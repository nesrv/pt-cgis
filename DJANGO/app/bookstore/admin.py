from django.contrib import admin
from .models import Book

admin.site.site_header = "Админка"
admin.site.index_title = "Книжный магазин"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')    
    list_display_links = ('title', 'author')    
    ordering = ['id']