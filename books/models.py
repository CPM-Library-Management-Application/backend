from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=256)
    def __str__(self):
        return self.name

