from django.db import models

class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=50)
    poster_url = models.TextField(default='')
    genre = models.CharField(max_length=30)
    showtime = models.CharField(max_length=4)
    release_date = models.CharField(max_length=15)
    plot = models.TextField(default='')
    rating = models.CharField(max_length=10)
    director_name = models.CharField(max_length=30)
    director_image_url = models.TextField(default='')
    
class Actor(models.Model):
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE, related_name='actors')
    name = models.CharField(max_length=30)
    character = models.CharField(max_length=30)
    image_url = models.TextField(default='')

"""
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    """