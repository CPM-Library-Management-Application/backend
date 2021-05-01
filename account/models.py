from django.db import models


# Create your models here.

class UserDetails(models.Model):
    qrcode = models.ImageField(null=True, upload_to="user_qrcodes")
