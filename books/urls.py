from django.urls import path
from .views import book_list, add_book, update_availability, my_book_list, delete_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('my_books/', my_book_list, name='my_book_list'),
    path('add/', add_book, name='add_book'),
    path('<int:book_id>/update/', update_availability, name='update_availability'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
]
