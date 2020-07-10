from django import forms

from .models import Phone, Bid


class PhoneCreationForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'image', 'condition', 'operating_system', 'colour', 'storage_capacity',
                  'ram', 'processor_type', 'processor_speed', 'camera', 'screen_type', 'screen_size', 'notes']
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(PhoneCreationForm, self).__init__(*args, **kwargs)


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        exclude = ('account', 'auction')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(BidForm, self).__init__(*args, **kwargs)
