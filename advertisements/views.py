from django.shortcuts import render

from advertisements.models import Advert


def list_view(request):
    adverts = Advert.objects.all()
    return render(request, 'adverts.html', context={'adverts': adverts})
