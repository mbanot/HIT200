from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'auctionAPI'

router = DefaultRouter()
router.register('bid', views.BidViewSet)

urlpatterns = [
    url(r'', include(router.urls), name='bid')
]