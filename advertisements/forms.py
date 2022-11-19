from django import forms

from advertisements.models import Advert, Category


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = "__all__"
        exclude = ('is_active', 'user',)


class AdvertFilterForm(forms.ModelForm):

    title = forms.CharField(required=False)
    city = forms.CharField(required=False)
    category = forms.MultipleChoiceField(choices=[(c.pk, c.name) for c in Category.objects.all()], required=False)
    class Meta:
        model = Advert
        fields = ('title', 'city', 'category',)
