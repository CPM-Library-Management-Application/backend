# Generated by Django 3.1.7 on 2021-04-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='x_coordinate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='y_coordinate',
            field=models.IntegerField(null=True),
        ),
    ]