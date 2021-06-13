from django.db import models


# Create your models here.


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, null=True)
    author = models.CharField(max_length=40, null=True)
    genre = models.CharField(max_length=40, null=True)
    lease_expiration_date = models.DateField(null=True)
    current_owner = models.ForeignKey(to="account.User", related_name="user", blank=True, on_delete=models.CASCADE)
    library_id = models.ForeignKey(to="Library", related_name="library", on_delete=models.DO_NOTHING)
    qrcode = models.ImageField(null=True, upload_to="qr_codes")

    def __str__(self):
        return self.title


class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=True)
    x_coordinate = models.FloatField(null=True)
    y_coordinate = models.FloatField(null=True)
    books = models.ManyToManyField(to="Book", related_name='books', blank=True)

    def __str__(self):
        return self.name
