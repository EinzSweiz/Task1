from django.db import models
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string

class ShortenedUrl(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = get_random_string(6)
        super().save(*args, **kwargs)


    