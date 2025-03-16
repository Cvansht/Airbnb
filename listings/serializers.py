from rest_framework import serializers
from .models import AirbnbListing

class AirbnbListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirbnbListing
        fields = '__all__'
