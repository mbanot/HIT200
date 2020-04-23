from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'condition', 'notes', 'category']
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(ProductForm, self).__init__(*args, **kwargs)
