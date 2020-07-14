from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
import datetime

from django.views.generic.base import View

from .forms import PhoneCreationForm, AuctionStartForm
from .models import Phone, Category, Auction, Bid


def index_view(request):
    template_name = 'index.html'

    phonesAuction = Auction.objects.filter(model_type='Phone', ending_date_and_time__gte=now(),
                                     starting_date_and_time__lte=now())
    bid = Bid.objects.all()
    phones = Phone.objects.all()
    context = {
        'categories': Category.objects.all().order_by('category'),
        'phonesAuction': phonesAuction,
        'phones': phones,
        'bid': bid,
    }
    return render(request, template_name, context)


def create_product(request):
    template_name = 'auction/add_product.html'
    context = {
        'categories': Category.objects.all().order_by('category')
    }
    return render(request, template_name, context)


class PhoneCreateView(CreateView):
    template_name = 'auction/phone_form.html'
    form_class = PhoneCreationForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('auction:create-product'))
        # return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PhoneCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['account'] = self.request.user
        return kwargs


def my_products(request):
    template_name = 'auction/product_list.html'
    context = {
        'phones': Phone.objects.filter(account=request.user)
    }
    return render(request, template_name, context)


class PhoneListView(ListView):
    model = Phone

    def get_context_data(self, **kwargs):
        context = super(PhoneListView, self).get_context_data(**kwargs)
        context['phone_list'] = Phone.objects.filter(account=self.request.user)
        return context
    paginate_by = 20


class PhoneDetailView(DetailView):
    model = Phone
    context_object_name = 'phone_list'

    def get_context_data(self, **kwargs):
        context = super(PhoneDetailView, self).get_context_data(**kwargs)
        context["phone"] = Phone.objects.get(id=self.kwargs['pk'])
        return context


class PhoneUpdateView(UpdateView):
    model = Phone
    fields = ['brand', 'model', 'image', 'condition', 'operating_system', 'colour', 'storage_capacity',
              'ram', 'processor_type', 'processor_speed', 'camera', 'screen_type', 'screen_size', 'notes']


class AuctionStart(View):
    template_name = 'auction/auction_form.html'
    form_class = AuctionStartForm

    def get(self, request):
        form = self.form_class(None)
        form.model_type = self.request.POST['model_type']
        form.product_id = self.request.POST['product_id']
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auction:my-products'))
        return render(request, self.template_name, {'form': form})


class CurrentAuctionsListView(ListView):
    model = Auction

    def get_queryset(self):
        # Auction.objects.filter(content_type=content_type, date_end__gte=now(),
        #                                            date_start__lte=now())
        return Auction.objects.filter(ending_date_and_time__gte=now(), starting_date_and_time__lte=now())

    def get_context_data(self, **kwargs):
        context = super(CurrentAuctionsListView, self).get_context_data(**kwargs)
        context['account'] = self.request.user
        return context


class ClosedAuctionsListView(ListView):
    model = Auction

    def get_queryset(self):
        return Auction.objects.filter(product__account=self.request.user, ending_date_and_time__lte=now())

    def get_context_data(self, **kwargs):
        context = super(ClosedAuctionsListView, self).get_context_data(**kwargs)
        context['account'] = self.request.user
        return context


# @login_required(redirect_field_name='/auction/dashboard/', login_url='/account/login/')
# def dashboard(request):
#     template_name = 'auction/dashboard.html'
#     context = {
#         'products': Product.objects.filter(account=request.user),
#         'auction_list': Auction.objects.filter(product__account=request.user,
#                                                date_end__gte=now(), date_start__lte=now()),
#         'bid_list': Bid.objects.filter(account=request.user),
#         # 'form': ProductForm(request.GET, instance=request.user)
#     }
#     if request.POST:
#         form = ProductForm(request.POST)
#         # if form.is_valid():
#         # form.save()
#
#         if form.is_valid():
#             object = form.save(commit=False)
#             object.account = request.user
#             object.save()
#         # context['account'] = request.user
#
#     else:
#         form = ProductForm()
#     context['form'] = form
#
#     return render(request, template_name, context)

#
# def auction_floor_view(request):
#     template_name = 'auction/auction_list.html'
#     context = {
#         'auction_list': Auction.objects.filter(ending_date_and_time__gte=now(), starting_date_and_time__lte=now()),
#         'categories': Category.objects.all().order_by('category'),
#         'bid_list': Bid.objects.all(),
#         'phones': Auction.objects.filter(model_type='Phone')
#     }
#     return render(request, template_name, context)


def filter_auctions(request):
    return request


def watchlist_page(request):
    return request


def detail_view(request, pk):
    template_name = 'auction/auction_detail.html'
    auction = Auction.objects.filter(product_id=pk)[0]
    bid = Bid.objects.filter(auction_id=auction.id).last()
    phones = Phone.objects.all()
    context = {
        'auction': auction,
        'phones': phones,
        'bid': bid,
    }
    return render(request, template_name, context)


# class AuctionDetailView(DetailView):
#     model = Auction
#     context_object_name = 'auction_list'
#
#     def get_context_data(self, **kwargs):
#         context = super(AuctionDetailView, self).get_context_data(**kwargs)
#         context["auction"] = Auction.objects.get(product_id=self.kwargs['pk'])
#         context['bid'] = Bid.objects.filter(auction=self.kwargs['pk']).last
#         return context


class BidderListView(ListView):
    model = Bid

    def get_queryset(self):
        return Bid.objects.filter(auction_id=self.kwargs['pk']).order_by('timestamp').reverse()

    def get_context_data(self, **kwargs):
        context = super(BidderListView, self).get_context_data(**kwargs)
        context['auction_id'] = self.kwargs['pk']
        return context


def save_bid(request):
    context = dict()
    context['auction_list'] = Auction.objects.get(id=request.POST.get('auction_id'))
    context['auction'] = Auction.objects.get(id=request.POST.get('auction_id'))
    if request.method == 'POST':
        if int(request.POST.get('starting_bid')) > int(request.POST.get('amount')):
            context['error'] = "Bid amount should be more than the starting bid"
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
                if not a:
                    obj = Bid(account=request.user, auction=Auction.objects.get(id=request.POST.get('auction_id')),
                              amount=int(request.POST.get('amount')))
                    obj.save()
                    context['alert'] = "The bid has been successfully made."
                    # auction = Auction.objects.get(id=request.POST.get('auction_id'))
                    return HttpResponseRedirect(reverse('auction:index'))
    return render(request, 'auction/auction_detail.html', context)


class PhoneDeleteView(DeleteView):
    model = Phone

    def get_context_data(self, **kwargs):
        context = super(PhoneDeleteView, self).get_context_data(**kwargs)
        context['product_id'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('auction:my-phones')

    def post(self, request, *args, **kwargs):
        if "Cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(PhoneDeleteView, self).post(request, *args, **kwargs)
