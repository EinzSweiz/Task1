# views.py
from django.shortcuts import redirect, render
from .forms import ShortenedUrlForm
from .models import ShortenedUrl

def shorten_url_view(request):
    if request.method == 'POST':
        form = ShortenedUrlForm(request.POST)
        if form.is_valid():
            shortened_url_instance = form.save()  # Save the form instance
            return redirect('shorturls:shortened_url', shortened_url=shortened_url_instance.short_url)
    else:
        form = ShortenedUrlForm()
    return render(request, 'shorturls/index.html', {'form': form})

def shortened_url_view(request, shortened_url):
    # Retrieve the URL instance using the short_url field
    try:
        url_instance = ShortenedUrl.objects.get(short_url=shortened_url)
        return render(request, 'shorturls/shortened.html', {'shortened_url': url_instance})
    except ShortenedUrl.DoesNotExist:
        return render(request, 'shorturls/shortened.html', {'error': 'URL not found'})


def all_links_view(request):
    qs = ShortenedUrl.objects.all()
    return render(request, 'shorturls/all_links.html', {'qs':qs})