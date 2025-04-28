from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=80)
    website = models.URLField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Watch_list(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,related_name="Watch_list")
    active =    models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    Watch_list= models.ForeignKey(Watch_list,on_delete=models.CASCADE,related_name="reviews")
    
    def __str__(self):
        return str(self.rating) + str(self.Watch_list.title)