from django.shortcuts import render
from website import models
from .forms import SiteSettingsForm


def update_settings(request):
    setting = models.SiteSetting.objects.all().first()
    form = SiteSettingsForm(instance=setting)
    return render(request, 'change-settings.html', {'form': form})
