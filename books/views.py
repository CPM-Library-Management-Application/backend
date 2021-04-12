from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, LibrarySerializer
from .models import Book,Library


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('name')
    serializer_class = LibrarySerializer
