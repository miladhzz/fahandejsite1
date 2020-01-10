from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from website import models
from .forms import SiteSettingsForm
from django.contrib.auth import logout


@login_required
def update_settings(request):
    setting = models.SiteSetting.objects.all().first()
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, instance=setting)
        if form.is_valid():
            setting = form.save()
            setting.save()
    else:
        form = SiteSettingsForm(instance=setting)
    return render(request, 'change-settings.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('website:index')
