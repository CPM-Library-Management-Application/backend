from django.urls import path
from .views import books_view, library_view, library_view_by_id, book_view, lease_book, return_book,add_book_to_library, reserve_book, search_book


urlpatterns = [
    path('books/<int:id>', book_view),
    path('books/<int:id>/lease', lease_book),
    path('books/<int:id>/reserve', reserve_book),
    path('books/<int:id>/return', return_book),
    path('books/', add_book_to_library),
    path('books/search', search_book),

    path('library/', library_view),
    path('library/<int:library_id>', library_view_by_id),
    path('library/<int:library_id>/books', books_view)
]
