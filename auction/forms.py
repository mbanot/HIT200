from django import forms
from .models import Phone, Bid, Auction


class PhoneCreationForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = ['brand', 'model', 'image', 'condition', 'operating_system', 'colour', 'storage_capacity',
                  'ram', 'processor_type', 'processor_speed', 'camera', 'screen_type', 'screen_size', 'notes']
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(PhoneCreationForm, self).__init__(*args, **kwargs)


class AuctionStartForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ['starting_date_and_time', 'ending_date_and_time', 'starting_bid', 'bid_increment',
                  'product_id', 'model_type']
        widgets = {
            'product_id': forms.HiddenInput(),
            'model_type': forms.HiddenInput()
        }

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['content_object'] = self.request.POST['content_object']
    #     return initial
    #
    # def __init__(self, *args, **kwargs):
    #     super(AuctionStartForm, self).__init__(*args, **kwargs)


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']
        exclude = ('account', 'auction')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super(BidForm, self).__init__(*args, **kwargs)
