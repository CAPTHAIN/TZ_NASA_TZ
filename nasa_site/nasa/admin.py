from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'photo', 'date')
    list_display_links = ('title', 'photo')
    search_fields = ('title',)
    list_filter = ('date',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'


admin.site.register(Post, PostAdmin)

admin.site.site_title = 'Админ панель сайта NASA'
admin.site.site_header = 'Админ панель сайта NASA'