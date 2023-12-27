from django.urls import path, include
from . import views
urlpatterns = [
    path("books/", include(
        [
            path("", views.book_list, name="book_list"),
            path("my_books/", views.my_book_list, name="my_book_list"),
            path("add/", views.add_book, name="add_book"),
            path("<int:book_id>/update/", views.update_availability, name="update_availability"),
            path("<int:book_id>/delete/", views.delete_book, name="delete_book"),
        ]
    ))
]
