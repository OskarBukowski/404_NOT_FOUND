from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from advertisements.forms import AdvertForm, AdvertFilterForm, ImageForm
from advertisements.models import Advert, Image


def list_view(request):
    adverts = Advert.objects.all()
    filter_form = AdvertFilterForm(request.GET or None)
    if filter_form.is_valid():
        if title := filter_form.cleaned_data.get('title', '').strip():
            adverts = adverts.filter(title__icontains=title)
        if city := filter_form.cleaned_data.get('city', '').strip():
            adverts = adverts.filter(city__icontains=city)
        if category := filter_form.cleaned_data.get('category', ''):
            adverts = adverts.filter(category__in=category)

        adverts = adverts.order_by(filter_form.cleaned_data.get('post_date') or '-post_date')

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


def showimage(request):
    lastimage = Image.objects.last()
    imagefile = lastimage.imagefile
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    return render(request, 'image.html', context)
