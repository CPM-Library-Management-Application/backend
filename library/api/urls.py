from django.urls import path
from .views import books_view, library_view, library_view_by_id, book_view

urlpatterns = [
    path('book/<int:book_id>', book_view),
    path('library/', library_view),
    path('library/<int:library_id>', library_view_by_id),
    path('library/<int:library_id>/books', books_view)

]