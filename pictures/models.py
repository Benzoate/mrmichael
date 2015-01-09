import os
from django.db import models
from django.utils import translation
from django.conf import settings
from django_thumbs.db.models import ImageWithThumbsField
from pages import models as page_models


class Album(page_models.Streamable):
    ALBUM_TYPES = (
        ('NORMAL', 'Normal Album'),
        ('PAGE', 'Page images'),
        ('HEAD', 'Page headers'),
    )
    thumbnail = models.ForeignKey('AlbumImage', related_name='thumbnail',
                                  blank=True, null=True)
    type = models.CharField(choices=ALBUM_TYPES, max_length=6,
                            default='NORMAL')

    def get_album_information(self, lang=None):
        if not lang:
            lang = translation.get_language()
        try:
            info = AlbumInformation.objects.get(language=lang, album=self)
        except AlbumInformation.DoesNotExist:
            if '-' not in lang:
                if lang == settings.LANGUAGE_CODE:
                    return None
                return self.get_album_information(lang=settings.LANGUAGE_CODE)
            try:
                info = AlbumInformation.objects.get(language=lang[:2],
                                                    album=self)
            except AlbumInformation.DoesNotExist:
                if lang == settings.LANGUAGE_CODE:
                    return None
                return self.get_album_information(lang=settings.LANGUAGE_CODE)
        return info

    def stream_title(self):
        try:
            return self.get_album_information().title
        except AttributeError:
            return 'Untitled'

    def stream_url(self):
        return '/pictures/album/%s/' % (self.pk)

    def thumbnail_url(self):
        return '/pictures/thumb/%s/' % (self.thumbnail_id)

    def subtitle(self):
        try:
            return self.get_album_information().subtitle
        except AttributeError:
            return ''

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __unicode__(self):
        try:
            return self.name
        except AttributeError:
            self.name = self.stream_title()
            return self.name


class AlbumInformation(page_models.Translatable):
    title = models.TextField()
    subtitle = models.TextField()
    album = models.ForeignKey(Album)


class AlbumImage(models.Model):
    album = models.ForeignKey(Album)
    image = ImageWithThumbsField(sizes=((640, 480), ))

    def save(self, *args, **kwargs):
        super(AlbumImage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "AlbumImage"
        verbose_name_plural = "AlbumImages"

    def __unicode__(self):
        return os.path.basename(self.image.name)
