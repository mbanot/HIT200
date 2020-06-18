from rest_framework import serializers
from auction import models


class BidSerializer(serializers.ModelSerializer):
    """A serializer for our bids model"""

    class Meta:
        model = models.Bid
        fields = ('id', 'account', 'auction', 'amount', 'bid_time',)

    def create(self, validated_data):
        """Create a new bid"""

        bid = models.Bid(
            account=validated_data['account'],
            auction=validated_data['auction'],
            amount=validated_data['amount']
        )
        bid.save()

        return bid
