from .models import SiteSetting


def get_settings(request):
    return {'settings': SiteSetting.objects.all().first()}

