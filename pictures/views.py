import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from pictures import models

ON_HEROKU = os.environ.get('ON_HEROKU')


def index(request):
    albums = list(models.Album.objects.filter(published=True)
                  .order_by('-last_updated_date').all())
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
