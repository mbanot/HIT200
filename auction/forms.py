from django import forms
from .models import Product, Bid


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'condition', 'notes', 'category']
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(ProductForm, self).__init__(*args, **kwargs)


class BidsForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount', 'auction', 'account']

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('account')
            super(ProductForm, self).__init__(*args, **kwargs)
