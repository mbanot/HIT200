from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .forms import ProductForm
from .models import Product, Category, Auction


def index_view(request):
    template_name = 'index.html'
    context = {
        'auctions': Auction.objects.filter(date_end__gte=now(), date_start__lte=now()),
        'categories': Category.objects.order_by('category')
    }
    return render(request, template_name, context)


class ProductCreate(CreateView):
    template_name = 'auction/product_form.html'
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('auction:dashboard'))
        # return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ProductCreate, self).get_form_kwargs(*args, **kwargs)
        kwargs['account'] = self.request.user
        return kwargs


@login_required(redirect_field_name='/auction/dashboard/', login_url='/account/login/')
def dashboard(request):
    template_name = 'auction/dashboard.html'
    context = {
        'products': Product.objects.filter(account=request.user),
        # 'account': request.user
    }
    return render(request, template_name, context)


def auction_floor_view(request):
    template_name = 'auction/auction_floor.html'
    context = {
        'auctions': Auction.objects.filter(date_end__gte=now(), date_start__lte=now()),
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)


def filter_auctions(request):
    return request


def watchlist_page(request):
    return request


def detail_view(request, pk):
    template_name = 'auction/details.html'
    auction = Auction.objects.filter(id=pk)
    context = {
        'auction': auction,
    }
    return render(request, template_name, context)


class DetailView(DetailView):
    model = Auction
    template_name = 'auction/details.html'


def bid(request, auction_id):
    pass
