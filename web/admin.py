from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 'content', 'created', 'updated', 'publicated', 'author'
    )
    list_editable = ('publicated', )
    list_display = (
        'id', 'title', 'created', 'updated', 'publicated', 'author'
    )
    search_fields = (
        'id', 'title', 'created', 'updated', 'publicated', 'author'
    )
    readonly_fields = (
        'id', 'created', 'updated'
    )

admin.site.register(News, NewsAdmin)