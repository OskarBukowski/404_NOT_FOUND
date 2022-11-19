from django.shortcuts import render
from advertisements.forms import AdvertForm
from advertisements.models import Advert


def list_view(request):
    adverts = Advert.objects.all()
    return render(request, 'adverts.html', context={'adverts': adverts})


def single_advert(request, pk):
    advert = Advert.objects.get(pk=pk)
    return render(request, 'advert_detail.html', context={'advert': advert})


def create_advert(request):
    form = AdvertForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('adverts')
    return render(request, 'advert_create.html', {'form': form})
