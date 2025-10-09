from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='place_covers/', blank=True, null=True)
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"{self.name} in {self.location}"


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=3
    )
    comment = models.CharField(max_length=255)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="reviews")
    place = models.ForeignKey("Place", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"Review by {self.user.username} on {self.place.name}"

class ReviewImage(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='review_images/')
    
    def __str__(self):
        return f"Image for review {self.review.id}"
