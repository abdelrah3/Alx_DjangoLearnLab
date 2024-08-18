import django
import os

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(f"Book Title: {book.title}")

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Book Title: {book.title}")
    except Library.DoesNotExist:
        print("Library does not exist.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian Name: {librarian.name}")
    except Library.DoesNotExist:
        print("Library does not exist.")
    except Librarian.DoesNotExist:
        print("Librarian does not exist.")

# Example usage
if __name__ == "__main__":
    print("Books by Author 'John Doe':")
    query_books_by_author('John Doe')

    print("\nBooks in Library 'Central Library':")
    list_all_books_in_library('Central Library')

    print("\nLibrarian for Library 'Central Library':")
    retrieve_librarian_for_library('Central Library')
