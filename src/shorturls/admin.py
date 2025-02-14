from django.contrib import admin
from .models import ShortenedUrl

@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'short_url']