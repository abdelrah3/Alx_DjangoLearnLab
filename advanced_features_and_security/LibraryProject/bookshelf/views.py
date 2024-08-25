from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import ExampleForm

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    books = Book.objects.filter(title=user_input)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Logic to create a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit the book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    # Redirect after deletion
    pass
