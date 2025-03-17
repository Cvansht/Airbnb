from django.urls import path
from .views import get_listings, add_listing

urlpatterns = [
    path('listings/', get_listings, name="get_listings"),
    path('add_listing/', add_listing, name="add_listing"),
]
