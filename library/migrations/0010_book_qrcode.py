# Generated by Django 3.1.7 on 2021-05-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20210425_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qrcode',
            field=models.ImageField(null=True, upload_to='qr_codes'),
        ),
    ]
