from django.shortcuts import render, get_object_or_404
from pages import models
from django.utils import translation


def index(request):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    pages = (models.Page.objects.filter(published=True)
             .order_by('-last_updated_date').all())
    return render(request, 'pages/index.html', {'pages': pages})


def view_page(request, path):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    page = get_object_or_404(models.Page, url=path)
    return render(request, 'pages/index.html', {'pages': [page]})
