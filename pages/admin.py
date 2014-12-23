from django.contrib import admin
from django import forms
from pages import models


class PageTextInlineForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = models.PageText


class PageTextInline(admin.TabularInline):
    form = PageTextInlineForm
    model = models.PageText


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [
        PageTextInline,
    ]
