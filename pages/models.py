from django.db import models
from django.utils import translation
from django.conf import settings


class Streamable(models.Model):
    last_updated_date = models.DateTimeField()
    published = models.BooleanField(default=False)
    _my_subclass = models.CharField(max_length=200, editable=False)

    class Meta:
        verbose_name = "Streamable"
        verbose_name_plural = "Streamables"

    def __unicode__(self):
        return '%s' % (self.last_updated_date)

    def as_child(self):
        return getattr(self, self._my_subclass)

    def save(self, *args, **kwargs):
        self._my_subclass = self.__class__.__name__.lower()
        super(Streamable, self).save(*args, **kwargs)

    def stream_title(self):
        return self.as_child().stream_title()

    def stream_url(self):
        return self.as_child().stream_url()


class Translatable(models.Model):
    from django.conf import settings
    language = models.CharField(max_length=7, choices=settings.LANGUAGES)

    class Meta:
        verbose_name = "Translatable"
        verbose_name_plural = "Translatables"

    def __unicode__(self):
        return self.language


class Page(Streamable):
    url = models.CharField(max_length=20, default='', blank=True)
    header_bg = models.CharField(max_length=128, default='', blank=True)

    def get_page_text(self, lang=None):
        if not lang:
            lang = translation.get_language()
        try:
            text = PageText.objects.get(language=lang, page=self)
        except PageText.DoesNotExist:
            if '-' not in lang:
                if lang == settings.LANGUAGE_CODE:
                    return None
                return self.get_page_text(lang=settings.LANGUAGE_CODE)
            try:
                text = PageText.objects.get(language=lang[:2], page=self)
            except PageText.DoesNotExist:
                if lang == settings.LANGUAGE_CODE:
                    return None
                return self.get_page_text(lang=settings.LANGUAGE_CODE)
        return text

    @property
    def page_text(self):
        return self.get_page_text()

    def stream_url(self):
        return '/page/%s/' % self.url

    def stream_title(self):
        return self.get_page_text().title

    def __unicode__(self):
        try:
            txt = self.get_page_text()
            return '(%s)%s' % (self.last_updated_date, txt.title, )
        except AttributeError:
            return super(Page, self).__unicode__()

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class PageText(Translatable):
    title = models.TextField()
    text = models.TextField()
    page = models.ForeignKey(Page)

    class Meta:
        verbose_name = "PageText"
        verbose_name_plural = "PageTexts"

    def __unicode__(self):
        return '[%s]%s' % (self.language, self.title)
