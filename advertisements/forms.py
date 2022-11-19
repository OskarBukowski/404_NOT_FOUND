from django import forms

from advertisements.models import Advert, Category, Image


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = "__all__"
        exclude = ('is_active', 'user',)


class AdvertFilterForm(forms.ModelForm):
    ORDER_CHOICES = (
        ('title', 'title ASC'),
        ('-title', 'title DESC'),
        ('post_date', 'date ASC'),
        ('-post_date', 'date DESC'),)

    category = forms.ChoiceField(choices=[(c.pk, c.name) for c in Category.objects.all()], required=False)
    title = forms.CharField(required=False)
    city = forms.CharField(required=False)
    # post_date = forms.ChoiceField(choices=ORDER_CHOICES)

    class Meta:
        model = Advert
        fields = ('title', 'city',)




class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("name", "imagefile",)
