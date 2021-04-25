from django.db import models


# Create your models here.


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, null=True)
    author = models.CharField(max_length=40, null=True)
    genre = models.CharField(max_length=40, null=True)
    lease_expiration_date = models.DateField(null=True)
    current_owner = models.CharField(max_length=300, null=True)
    library_id = models.OneToOneField("Library", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=True)
    x_coordinate = models.IntegerField(null=True)
    y_coordinate = models.IntegerField(null=True)
    books = models.ManyToManyField(to="Book", related_name='books')

    def __str__(self):
        return self.name