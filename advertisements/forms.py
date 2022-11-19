from django import forms

from advertisements.models import Advert


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = "__all__"
        exclude = ('is_active',)
