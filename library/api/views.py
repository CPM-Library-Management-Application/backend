from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from ..models import Book, Library
from .serializers import BookSerializer, LibrarySerializer


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
def book_view(request, book_id):
    if request.method == 'GET':
        pass
        # books = Book.objects.filter(library_id=library_id)
        # serializer = BookSerializer(books, many=True)

        # return JsonResponse(serializer.data, safe=False)


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
