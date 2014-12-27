from django.contrib import admin
from pictures import models
from django import forms


class AlbumInformationInlineForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput, label='title')
    subtitle = forms.CharField(widget=forms.TextInput, label='subtitle')

    class Meta:
        model = models.AlbumInformation
        fields = '__all__'


class AlbumInformationInline(admin.TabularInline):
    form = AlbumInformationInlineForm
    model = models.AlbumInformation


class AlbumImageInline(admin.TabularInline):
    model = models.AlbumImage


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        AlbumInformationInline,
        AlbumImageInline
    ]
