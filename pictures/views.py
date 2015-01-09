import os
import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import translation
from pictures import models, forms

ON_HEROKU = os.environ.get('ON_HEROKU')


def index(request):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    albums = models.Album.objects
    if not request.user.is_superuser:
        albums = albums.filter(published=True)
    albums = list(albums.order_by('-last_updated_date').all())
    albums = map(lambda x: {'album': x,
                            'info': x.get_album_information(),
                            'thumbnail': x.thumbnail_url(),
                            'url': x.stream_url()},
                 albums)
    dick = {
        'is_pictures': True,
        'albums': albums
    }
    return render(request, 'pictures/index.html', dick)


def album(request, album_id):
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    if album_id == 'new':
        new_album = models.Album()
        new_album.last_updated_date = datetime.datetime.now()
        new_album.save()
        return redirect('/pictures/album/%s/' % new_album.pk)
    album = get_object_or_404(models.Album, pk=album_id)
    informations = models.AlbumInformation.objects.filter(album=album).values()
    images = list(models.AlbumImage.objects.filter(album=album).all())
    images = map(lambda x: {'id': x.pk,
                            'thumb': '/pictures/thumb/%s/' % x.pk,
                            'full': '/pictures/image/%s/' % x.pk}, images)
    dic = {
        'is_pictures': True,
        'album': album,
        'informations': informations,
        'images': images
    }
    return render(request, 'pictures/album.html', dic)


def upload_image(request, album_id):
    if request.method == 'POST':
        form = forms.AlbumImageUploadForm(request.POST, request.FILES)
        new_item = form.save()

        return HttpResponse(new_item.pk)


def get_image(request, pk):
    image = get_object_or_404(models.AlbumImage, pk=pk)
    if not ON_HEROKU:
        filename = image.image.file.name.split('/')[-1]
        response = HttpResponse(image.image.file,
                                content_type=('image/%s' % (filename[-3:])))
        return response

    return redirect(image.image.url)


def get_thumbnail(request, pk):
    image = get_object_or_404(models.AlbumImage, pk=pk)
    if not ON_HEROKU:
        filename = image.image.file.name.split('/')[-1]
        response = HttpResponse(image.image.file,
                                content_type=('image/%s' % (filename[-3:])))
        return response

    return redirect(image.image.url_640x480)
