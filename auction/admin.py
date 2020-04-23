from django.contrib import admin
from .models import Product, Category, Auction

admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Category)
