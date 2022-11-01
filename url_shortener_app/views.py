from django.shortcuts import render, redirect
from .models import URL
from .backend.short_url import ShortURL

def home(request):
    return render(request, 'url_shortener_app/home.html')

def create_url(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        # short_url = request.POST.get("short_url")
        ttl = request.POST.get("ttl")
        short_url = ShortURL.get_short_url()
        url = URL(long_url=long_url, short_url=short_url, ttl=ttl)
        url.save()
        return redirect('/detail/'+str(url.id))
    return render(request, 'url_shortener_app/create_url.html')

def detail(request, url_id):
    url_info = URL.objects.get(id=url_id)
    return render(request, 'url_shortener_app/detail.html', {'url_info': url_info})

def delete(request, url_id):
    return render(request, 'url_shortener_app/cnfrm_delete.html', {'url_id': url_id})

def cnfrm_delete(request, url_id):
    url_info = URL.objects.get(id=url_id)
    url_info.delete()
    return redirect('/')

def view_urls(request):
    urls = URL.objects.all()
    return render(request, 'url_shortener_app/view_urls.html', {'urls': urls})


