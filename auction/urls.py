from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from auction import views

app_name = 'auction'

urlpatterns = [
    url(r'^add_product/$', login_required(views.create_product), name='create-product'),
    url(r'^add_phone/$', login_required(views.PhoneCreateView.as_view()), name='add-phone'),
    # url(r'^my_products/$', login_required(views.ProductListView.as_view()), name='my-products'),
    # url(r'^my_products/(?P<pk>[0-9]+)/$', login_required(views.ProductDetailView.as_view()), name='product_details'),
    # url(r'^my_products/edit/(?P<pk>[0-9]+)/$', views.ProductUpdateView.as_view(), name='update-product'),
    url(r'^current_auctions/$', login_required(views.CurrentAuctionsListView.as_view()), name='current-auctions'),
    url(r'^closed_auctions/$', login_required(views.ClosedAuctionsListView.as_view()), name='closed-auctions'),
    url(r'^$', views.index_view, name='index'),
    url(r'^index/$', views.index_view, name='index'),
    url(r'^auction_floor/$', views.auction_floor_view, name='auction-floor'),
# url(r'^auction_floor/$', views.AuctionFloorView.as_view(), name='auction-floor'),
#     url(r'^dashboard/$', login_required(views.dashboard), name='dashboard'),
    url(r'^category/<str:category>/$', views.filter_auctions, name='filter-auctions'),
    url(r'^watchlist/$', views.watchlist_page, name='watchlist'),
    url(r'^(?P<pk>[0-9]+)/$', views.AuctionDetailView.as_view(), name="details"),
    url(r'^save_bid/', login_required(views.save_bid), name="save-bid"),
    url(r'^bidder_list/(?P<pk>[0-9]+)/$', views.BidderListView.as_view(), name="bidder-list"),
    # url(r'delete_product/(?P<pk>[0-9]+)/$', login_required(views.ProductDeleteView.as_view()), name='delete-product'),
]
