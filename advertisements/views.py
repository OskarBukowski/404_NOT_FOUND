from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from advertisements.forms import AdvertForm, AdvertFilterForm
from advertisements.models import Advert


def list_view(request):
    adverts = Advert.objects.all()
    filter_form = AdvertFilterForm(request.POST or None)
    return render(request, 'adverts.html', context={'form': filter_form, 'adverts': adverts})


def single_advert(request, pk):
    advert = Advert.objects.get(pk=pk)
    return render(request, 'advert_detail.html', context={'advert': advert})


@login_required
def create_advert(request):
    advert = Advert(user=request.user)
    form = AdvertForm(request.POST or None, instance=advert)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('adverts')
    return render(request, 'advert_create.html', {'form': form})


def filter_adverts(request):
    form = AdvertFilterForm(request.POST or None)
    return render(request, 'advert_filter.html', {'form': form})
