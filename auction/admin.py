from django.contrib import admin
from .models import Phone, Category, Auction, Bid

admin.site.register(Phone)
admin.site.register(Auction)
admin.site.register(Category)
admin.site.register(Bid)
