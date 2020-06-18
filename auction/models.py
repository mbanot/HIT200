from django.db import models
from django.urls import reverse
from account.models import Account


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Product(models.Model):

    CONDITION = (
        ('New', 'New'),
        ('Used', 'Used'),
        ('Mint', 'Mint'),
        ('Boxed', 'Boxed'),
    )

    title = models.CharField(max_length=225)
    image = models.ImageField()
    condition = models.CharField(max_length=10, choices=CONDITION, default='NEW')
    notes = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def get_absolute_url(self):
        # if self.category == 'Laptops':
        #     return reverse('laptops')
        # else:
        return reverse('dashboard')

    def __str__(self):
        return self.title


class Auction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    current_bid = models.DecimalField(verbose_name='current winning bid', decimal_places=2, max_digits=11, default=0.00)
    date_start = models.DateTimeField(verbose_name='auction start date', auto_created=True)
    date_end = models.DateTimeField(verbose_name='auction end date', auto_created=True)
    start_bid = models.DecimalField(verbose_name='starting bid amount', decimal_places=2, default=1.00, max_digits=11)
    reserve_price = models.DecimalField(verbose_name='reserve price', decimal_places=2, max_digits=11,
                                        blank=True, null=True)
    bid_increment = models.DecimalField(verbose_name='minimum incremental bid', decimal_places=2, max_digits=11,
                                        blank=True, null=True, default=1.00)

    def get_absolute_url(self):
        return reverse('auction:details', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.current_bid)


class Watchlist(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='bid amount', default=0.00, decimal_places=2, max_digits=11)
    bid_time = models.DateTimeField(auto_now_add=True)
