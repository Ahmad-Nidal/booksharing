from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book

@login_required(login_url='login')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        owner = request.user
        Book.objects.create(title=title, author=author, owner=owner)
        return redirect('my_book_list')
    return render(request, 'books/add_book.html')

@login_required(login_url='login')
def update_availability(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.available_for_borrow = not book.available_for_borrow
    book.save()
    return redirect('my_book_list')

@login_required(login_url='login')
def my_book_list(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'books/my_book_list.html', {'books': books})

@login_required(login_url='login')
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('my_book_list')