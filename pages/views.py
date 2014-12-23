from django.shortcuts import render
from pages import models
from django.utils import translation


def index(request):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    pages = models.Page.objects.order_by('-last_updated_date').all()
    return render(request, 'pages/index.html', {'pages': pages})
