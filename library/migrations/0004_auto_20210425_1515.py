# Generated by Django 3.1.7 on 2021-04-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210422_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(related_name='books', to='library.Book'),
        ),
    ]