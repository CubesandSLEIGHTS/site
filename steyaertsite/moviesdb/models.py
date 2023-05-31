from django.db import models

# Create your models here.
class MovieList(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Movie(models.Model):
    movie_list = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=6)
    disk = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.title
