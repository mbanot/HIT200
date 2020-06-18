from rest_framework import viewsets
from auction import models
from . import serializers


class BidViewSet(viewsets.ModelViewSet):
    """Handles creating a bid"""

    serializer_class = serializers.BidSerializer
    queryset = models.Bid.objects.all()
