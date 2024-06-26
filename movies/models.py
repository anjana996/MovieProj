from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class MovieDetails(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    actors = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    trailer_link = models.URLField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

class MovieReviews(models.Model):
    movies = models.ForeignKey(MovieDetails,on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)

