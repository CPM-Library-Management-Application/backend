from django.contrib import admin
from .models import Library, Book


# Register your models here.
@admin.register(Library)
class LibraryDisplay(admin.ModelAdmin):
    list_display = ('library_id', 'name')


@admin.register(Book)
class BookDisplay(admin.ModelAdmin):
    list_display = ('book_id', 'author', 'title')
