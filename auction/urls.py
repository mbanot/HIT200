from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from auction import views

app_name = 'auction'

urlpatterns = [
    url(r'^add_product/$', login_required(views.create_product), name='create-product'),
    url(r'^add_phone/$', login_required(views.PhoneCreateView.as_view()), name='add-phone'),
    url(r'^edit_phone/(?P<pk>[0-9]+)/$', views.PhoneUpdateView.as_view(), name='update-phone' ),
    url(r'^my_products/$', login_required(views.my_products), name='my-products'),
    url(r'^my_products/phones/$', login_required(views.PhoneListView.as_view()), name='my-phones'),
    url(r'^my_products/phones/(?P<pk>[0-9]+)/$', login_required(views.PhoneDetailView.as_view()), name='phone-details'),
    url(r'my_products/start_auction/$', login_required(views.AuctionStart.as_view()), name='start-auction'),
    url(r'^current_auctions/$', login_required(views.current_auctions_view), name='current-auctions'),
    url(r'^closed_auctions/$', login_required(views.closed_auctions_view), name='closed-auctions'),
    url(r'^ongoing_auctions/$', login_required(views.ongoing_auctions_view), name='ongoing-auctions'),
    url(r'^$', views.index_view, name='index'),
    url(r'^index/$', views.index_view, name='index'),
    url(r'^phones_auctions_view/$', views.phones_auction_view, name='phones-auction-view'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail_view, name="details"),
    url(r'^save_bid/', login_required(views.save_bid), name="save-bid"),
    url(r'^bidder_list/(?P<pk>[0-9]+)/$', views.BidderListView.as_view(), name="bidder-list"),
    url(r'delete_phone/(?P<pk>[0-9]+)/$', login_required(views.PhoneDeleteView.as_view()), name='delete-phone'),
]
