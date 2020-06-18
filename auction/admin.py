from django.contrib import admin
from .models import Product, Category, Auction, Bid

admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Category)
admin.site.register(Bid)
