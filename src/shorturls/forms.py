from django import forms
from .models import ShortenedUrl


class ShortenedUrlForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ['original_url']