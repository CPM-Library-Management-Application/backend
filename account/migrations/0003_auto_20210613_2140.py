# Generated by Django 3.1.7 on 2021-06-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qrcode',
            field=models.ImageField(null=True, upload_to='user_qrcodes'),
        ),
    ]
