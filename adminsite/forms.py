from django import forms
from website import models
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import ugettext_lazy as _


class SiteSettingsForm(TranslationModelForm):
    class Meta:
        model = models.SiteSetting
        fields = ('address', 'phone', 'mobile', 'small_about', 'full_about', 'postal_code', 'email')
        labels = {
            'address': _('Address:'),
            'phone': _('Phone:'),
            'mobile': _('Mobile:'),
            'small_about': _('Small About:'),
            'full_about': _('Complete About:'),
            'postal_code': _('Postal Code:'),
            'email': _('Email:'),
        }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        error_messages = {
            'phone': {
                'max_length': _("Too many characters."),
                'required': _("This field is required."),
            },
        }
