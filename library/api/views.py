from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from ..models import Book, Library
from .serializers import BookSerializer, LibrarySerializer
import datetime


@api_view(['GET', ])
def books_view(request, library_id):
    if request.method == 'GET':
        params = request.query_params
        author = params.get('author', None)
        genre = params.get('genre', None)

        if author is None and genre is None:
            books = Book.objects.filter(library_id=library_id)
        elif author is not None and genre is None:
            books = Book.objects.filter(library_id=library_id, author=author)
        elif author is None and genre is not None:
            books = Book.objects.filter(library_id=library_id, genre=genre)
        elif author is not None and genre is not None:
            books = Book.objects.filter(library_id=library_id, author=author, genre=genre)

        serializer = BookSerializer(books, many=True)

        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', ])
def book_view(request, id):
    if request.method == 'GET':
        books = Book.objects.get(book_id=id)
        serializer = BookSerializer(books, many=False)

        return JsonResponse(serializer.data, safe=False)


@api_view(['POST', ])
def reserve_book(request, id):
    if request.method == 'POST':
        json_body = JSONParser().parse(request)

        book = Book.objects.get(book_id=id)
        book.current_owner = json_body['user']
        book.save()
        serializer = BookSerializer(book, many=False)

        return JsonResponse(serializer.data, safe=False)


@api_view(['POST', ])
def lease_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(book_id=id)
        book.lease_expiration_date = datetime.date.today() + datetime.timedelta(days=14)
        book.save()
        serializer = BookSerializer(book, many=False)

        return JsonResponse(serializer.data, safe=False)


@api_view(['POST', ])
def return_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(book_id=id)
        book.current_owner = None
        book.lease_expiration_date = None
        book.save()
        serializer = BookSerializer(book, many=False)

        return JsonResponse(serializer.data, safe=False)


@api_view(['POST', ])
def add_book_to_library(request):
    if request.method == 'POST':
        json_body = JSONParser().parse(request)

        library = Library.objects.get(library_id=json_body['library_id'])
        books = Book.objects.create(
            author=json_body['author'],
            title=json_body['title'],
            genre=json_body['genre'],
            library_id=library
        )
        serializer = BookSerializer(books, many=False)

        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def library_view(request):
    if request.method == 'GET':
        libraries = Library.objects.all()
        serializer = LibrarySerializer(libraries, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        json_body = JSONParser().parse(request)
        name = json_body['name']
        x = json_body['x_coordinate']
        y = json_body['y_coordinate']

        library = Library.objects.create(
            name=name,
            x_coordinate=x,
            y_coordinate=y
        )
        serializer = LibrarySerializer(library, many=False)

        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', ])
def library_view_by_id(request, library_id):
    if request.method == 'GET':
        libraries = Library.objects.get(library_id=library_id)
        serializer = LibrarySerializer(libraries, many=False)

        return JsonResponse(serializer.data, safe=False)
