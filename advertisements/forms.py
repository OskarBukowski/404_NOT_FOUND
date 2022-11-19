from django import forms

from advertisements.models import Advert, Category


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

    title = forms.CharField(required=False)
    city = forms.CharField(required=False)
    category = forms.MultipleChoiceField(choices=[(c.pk, c.name) for c in Category.objects.all()], required=False)
    post_date = forms.ChoiceField(choices=ORDER_CHOICES)

    class Meta:
        model = Advert
        fields = ('title', 'city',)
