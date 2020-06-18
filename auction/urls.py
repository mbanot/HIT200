from django.conf.urls import url
from auction import views

app_name = 'auction'

urlpatterns = [
    url(r'^add_product/$', views.ProductCreate.as_view(), name='create-product'),
    url(r'^$', views.index_view, name='index'),
    url(r'^index/$', views.index_view, name='index'),
    url(r'^auction_floor/$', views.auction_floor_view, name='auction-floor'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^category/<str:category>/$', views.filter_auctions, name='filter-auctions'),
    url(r'^watchlist/$', views.watchlist_page, name='watchlist'),
    url(r'^(?P<pk>[1-10]+)/$', views.DetailView.as_view(), name="details"),
    url(r'^submit_bid/', views.bid, name="bid"),
]
