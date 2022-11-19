from django.shortcuts import render
from advertisements.models import Advert


def list_view(request):
    adverts = Advert.objects.all()
    return render(request, 'adverts.html', context={'adverts': adverts})



def single_advert(request, id):
    advert = Advert.objects.get(pk=id)
    return render(request, 'advert_detail.html', context={'advert': advert})

