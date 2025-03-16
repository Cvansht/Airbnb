from django.db import models

class AirbnbListing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_urls = models.JSONField()  # Storing multiple images
    ratings = models.FloatField()
    description = models.TextField()
    num_reviews = models.IntegerField()
    amenities = models.JSONField()  # List of amenities
    host_info = models.JSONField()  # Host details
    property_type = models.CharField(max_length=100)

    def __str__(self):
        return self.title
