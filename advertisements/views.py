from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from advertisements.forms import AdvertForm, AdvertFilterForm, ImageForm
from advertisements.models import Advert, Image


def list_view(request):
    adverts = Advert.objects.all()
    filter_form = AdvertFilterForm(request.GET or None)
    if filter_form.is_valid():
        if category := filter_form.cleaned_data.get('category', ''):
            adverts = adverts.filter(category=category)
        if title := filter_form.cleaned_data.get('title', '').strip():
            adverts = adverts.filter(title__icontains=title)
        if city := filter_form.cleaned_data.get('city', '').strip():
            adverts = adverts.filter(city__icontains=city)

        adverts = adverts.order_by(filter_form.cleaned_data.get('order_by') or '-post_date')

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


def adverts_paginated(request):
    adverts = Advert.objects.all().order_by('-post_date')
    paginator = Paginator(adverts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'adverts.html', {'page_obj': page_obj})
