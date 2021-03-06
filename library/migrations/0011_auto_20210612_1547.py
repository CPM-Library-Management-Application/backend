# Generated by Django 3.1.7 on 2021-06-12 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_book_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='library_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='library', to='library.library'),
        ),
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='books', to='library.Book'),
        ),
        migrations.AlterField(
            model_name='library',
            name='x_coordinate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='y_coordinate',
            field=models.FloatField(null=True),
        ),
    ]
