from django.contrib import admin
from .models import UserDetails


# Register your models here.
@admin.register(UserDetails)
class LibraryDisplay(admin.ModelAdmin):
    list_display = ['qrcode']
