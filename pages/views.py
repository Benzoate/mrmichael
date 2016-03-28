from django.shortcuts import render, get_object_or_404
from pages import models
from django.utils import translation
from django.core.paginator import Paginator


def index(request):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    pages = (models.Page.objects.filter(published=True)
             .order_by('-last_updated_date').all())
    paginator = Paginator(pages, 5)
    num_pages = paginator.num_pages
    page_range = paginator.page_range

    try:
        page_idx = min(max(int(request.GET.get('page', 1)), 1),
                       paginator.num_pages)

        current_page = paginator.page(page_idx)
        pages = current_page.object_list
        prev_page = max(page_idx - 1, 1)
        next_page = min(page_idx + 1, num_pages)
    except ValueError: # Don't paginate if page is nonsense
        paginator = None
        num_pages = None
        page_range = None
        page_idx = None
        prev_page = None
        next_page = None

    return render(request, 'pages/index.html', {'pages': pages,
                                                'is_blog': True,
                                                'num_pages': num_pages,
                                                'current_page': page_idx,
                                                'page_range': page_range,
                                                'request': request,
                                                'previous_page': prev_page,
                                                'next_page': next_page,
                                                })


def view_page(request, path):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    page = get_object_or_404(models.Page, url=path)
    return render(request, 'pages/index.html', {'pages': [page],
                                                'is_blog': page.published,
                                                'is_about': path == 'about',
                                                'is_pictures': path == 'pictures',
                                                'is_resume': path == 'resume'})
