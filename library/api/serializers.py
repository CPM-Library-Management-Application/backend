from rest_framework import serializers
from ..models import Book, Library


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author','genre', 'lease_expiration_date', 'current_owner']


class LibrarySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Library
        fields = ['library_id', 'name', 'x_coordinate', 'y_coordinate', 'books']
