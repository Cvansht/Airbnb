from django.shortcuts import render

from rest_framework import generics
from .models import AirbnbListing
from .serializers import AirbnbListingSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = AirbnbListing.objects.all()
    serializer_class = AirbnbListingSerializer
