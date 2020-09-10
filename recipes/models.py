from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Recipe', related_name="favorite", symmetrical=False, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} - {self.author.name}"

