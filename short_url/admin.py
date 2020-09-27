from django.contrib import admin
from .models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'base_url', 'hash_url', 'created_at', 'clicks')
