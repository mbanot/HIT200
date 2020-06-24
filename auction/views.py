from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from account.models import Account
from .forms import ProductForm, BidForm
from .models import Product, Category, Auction, Bid


def index_view(request):
    template_name = 'index.html'
    amount = 0
    context = {
        'auctions': Auction.objects.filter(date_end__gte=now(), date_start__lte=now()),
        'categories': Category.objects.order_by('category'),
        'bid_list': Bid.objects.all(),
        'amount': amount
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
    template_name = 'auction/auction_list.html'
    context = {
        'auction_list': Auction.objects.filter(date_end__gte=now(), date_start__lte=now()),
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)


# class AuctionFloorView(ListView):
    model = Auction


def filter_auctions(request):
    return request


def watchlist_page(request):
    return request


def detail_view(request, pk):
    template_name = 'auction/auction_detail.html'
    auction = Auction.objects.filter(id=pk)
    context = {
        'auction': auction,
    }
    return render(request, template_name, context)


class AuctionDetailView(DetailView):
    model = Auction
    context_object_name = 'auction_list'

    def get_context_data(self, **kwargs):
        context = super(AuctionDetailView, self).get_context_data(**kwargs)
        # x = Auction.objects.all()
        context["auction"] = Auction.objects.get(product__auction=self.kwargs['pk'])
        context['bid'] = Bid.objects.filter(auction=self.kwargs['pk']).last
        return context


class BidderListView(ListView):
    model = Bid

    def get_queryset(self):
        return Bid.objects.filter(auction_id=self.kwargs['pk']).order_by('created').reverse()

    def get_context_data(self, **kwargs):
        context = super(BidderListView, self).get_context_data(**kwargs)
        context['auction_id'] = self.kwargs['pk']
        return context


def save_bid(request):
    context = dict()
    context['auction_list'] = Auction.objects.get(id=request.POST.get('auction_id'))
    context['auction'] = Auction.objects.get(id=request.POST.get('auction_id'))
    if request.method == 'POST':
        if int(request.POST.get('reserve_price')) > int(request.POST.get('amount')):
            context['error'] = "Bid amount should be more than reserve price"
            return render(request, 'auction/auction_detail.html', context)
        else:

            # if Bid.objects.filter(auction=Auction.objects.get(id=request.POST.get('auction_id'))):

            # obj, created = Bid.objects.update_or_create(account=request.user,
            #                                             auction=Auction.objects.get(request.POST.get('auction_id')),
            #                                             amount=int(request.POST.get('amount')))
            # created.save()
                x = Bid.objects.filter(auction=Auction.objects.get(id=request.POST.get('auction_id'))).values('account', 'auction')

                a = 0

                for item in x:
                    if item['account'] == request.user.id:
                        # y = Bid.objects.get(account=request.user.id, auction=Bid.objects.get(id=request.POST.get('auction_id')))
                        if item['auction'] == request.POST.get('auction_id'):
                            y = item
                            y.amount = int(request.POST.get('amount'))
                            y.save()
                            a = 1

                context['alert'] = "Reached stage 1"
                if not a:
                    context['alert'] = "Reached stage 2"
                    obj = Bid(account=request.user, auction=Auction.objects.get(id=request.POST.get('auction_id')),
                              amount=int(request.POST.get('amount')))
                    obj.save()
                    context['alert'] = "The bid has been successfully made."
                    # auction = Auction.objects.get(id=request.POST.get('auction_id'))
                    return HttpResponseRedirect(reverse('auction:auction-floor'))
    return render(request, 'auction/auction_detail.html', context)

