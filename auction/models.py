from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models
from django.urls import reverse
from account.models import Account


class Category(models.Model):

    category = models.CharField(max_length=30)
    view = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Phone(models.Model):

    CONDITION = (
        ('New', 'New'),
        ('Used', 'Used'),
        ('Mint', 'Mint'),
        ('Boxed', 'Boxed'),
    )

    OSCHOICE = (
        ("Android", "Android"),
        ("iOS", "iOS"),
        ("Windows", "Windows"),
        ("Other", "Other"),
    )

    brand = models.CharField(max_length=50, help_text="e.g. Samsung", null=False)
    model = models.CharField(max_length=50, help_text="e.g. S20", null=False)
    image = models.ImageField()
    condition = models.CharField(max_length=10, choices=CONDITION, default='NEW')
    operating_system = models.CharField(choices=OSCHOICE, max_length=10)
    colour = models.CharField(max_length=50)
    storage_capacity = models.CharField(max_length=25)
    ram = models.CharField(verbose_name="RAM size", max_length=50)
    processor_type = models.CharField(max_length=100)
    processor_speed = models.CharField(max_length=50, help_text="e.g. 2.1GHz")
    camera = models.CharField(max_length=50, help_text="e.g. 20 mega pixels")
    screen_size = models.CharField(max_length=50, help_text="e.g. 5.1 inches")
    screen_type = models.CharField(max_length=100)

    notes = models.TextField(max_length=250, help_text="Any other details that may help describe your phone")
    date_posted = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def get_absolute_url(self):
        # if self.category == 'Laptops':
        #     return reverse('laptops')
        # else:
        return reverse('auction:index')

    def __str__(self):
        return self.brand + ' ' + self.model


class Auction(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    current_bid = models.DecimalField(verbose_name='current winning bid', decimal_places=2, max_digits=11, default=0.00)
    date_start = models.DateTimeField(verbose_name='auction start date', auto_created=True)
    date_end = models.DateTimeField(verbose_name='auction end date', auto_created=True)
    start_bid = models.IntegerField(verbose_name='starting bid amount', default=1)
    reserve_price = models.IntegerField(verbose_name='reserve price', default=1)
    bid_increment = models.IntegerField(verbose_name='minimum incremental bid', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('auction:details', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.content_object)


class Watchlist(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='bid amount')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account)
