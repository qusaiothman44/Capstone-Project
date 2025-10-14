from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Place(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
 
    def get_absolute_url(self):
        return reverse('reviews:review_detail', kwargs={'pk': self.pk})
        
class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review= models.ForeignKey(Review,on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()
    date_created= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"commet {self.review.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField()
    avatar = CloudinaryField('avatar', default='5b078a59390bb4666df98b49f1cdedd0_t9ys7u') 
    def __str__(self):
       return f"{self.user.username}'s Profile"

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.review.title}"

