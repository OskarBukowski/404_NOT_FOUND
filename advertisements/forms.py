from django import forms

from advertisements.models import Advert, Category, Image


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = "__all__"
        exclude = ('is_active', 'user',)


class AdvertFilterForm(forms.Form):
    ORDER_CHOICES = (
        ('post_date', 'date ASC'),
        ('-post_date', 'date DESC'),)

    category = forms.ChoiceField(choices=[(c.pk, c.name) for c in Category.objects.all()], required=False)
    title = forms.CharField(required=False)
    city = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("name", "imagefile",)
