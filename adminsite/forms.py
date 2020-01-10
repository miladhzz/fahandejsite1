from django import forms
from website import models
from modeltranslation.forms import TranslationModelForm


class SiteSettingsForm(TranslationModelForm):
    class Meta:
        model = models.SiteSetting
        fields = ('address', 'phone', 'mobile', 'small_about', 'full_about', 'postal_code', 'email')
