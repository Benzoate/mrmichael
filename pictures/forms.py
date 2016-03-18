from django import forms
from pictures import models


class AlbumImageUploadForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = models.AlbumImage
