from django import forms
from django.views.decorators.clickjacking import xframe_options_sameorigin

from .models import Product, Bid


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'condition', 'notes', 'category']
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(ProductForm, self).__init__(*args, **kwargs)


@xframe_options_sameorigin
class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        exclude = ('account', 'auction')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(BidForm, self).__init__(*args, **kwargs)
