import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
import qrcode
from django.conf import settings
from django.dispatch import receiver
from pathlib import Path


class UserManager(models.Manager):
    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """

        now = datetime.datetime.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now)

        user.set_password(password)
        user.save(using=self._db)
        print(user.id)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    qrcode = models.ImageField(null=True, upload_to="user_qrcodes")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @receiver(models.signals.post_save)
    def user_created(sender, instance, created, **kwargs):
        root_path = settings.MEDIA_ROOT
        session_key = vars(instance).get("session_key", None)
        print("Sender: ", sender)
        print("Instance: ", instance)

        if created and session_key is None and "User" in str(sender):  ## :)
            qr = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
            qr.add_data(str(instance.id))
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

            path = Path(root_path + '/user_qrcodes/')
            path.mkdir(parents=True, exist_ok=True)

            img.save(root_path + "/user_qrcodes/qrcode" + str(instance.id) + ".png")

            instance.qrcode = "/user_qrcodes/qrcode" + str(instance.id) + ".png"
            instance.save()

