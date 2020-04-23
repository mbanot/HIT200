from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import ProductForm
from .models import Product, Category, Auction


# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = {'all_products'}
#
#     def get_queryset(self):
#         return Product.objects.all()
def index_view(request):
    template_name = 'index.html'
    context = {
        'auctions': Auction.objects.all(),
        'categories': Category.objects.order_by('category')}
    return render(request, template_name, context)


class ProductCreate(CreateView):
    template_name = 'auction/product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ProductCreate, self).get_form_kwargs(*args, **kwargs)
        kwargs['account'] = self.request.user
        return kwargs


@login_required(redirect_field_name='/auction/dashboard/', login_url='/account/login/')
def dashboard(request):
    template_name = 'auction/dashboard.html'
    context = {
        'products': Product.objects.all(),
        'account': request.user
    }
    return render(request, template_name, context)


def auction_floor_view(request):
    template_name = 'auction/auction_floor.html'
    context = {
        'auctions': Auction.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)


def filter_auctions(request):
    return request


def watchlist_page(request):
    return request
