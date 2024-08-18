from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
relationship_app/list_books.html
relationship_app/library_detail.html
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
