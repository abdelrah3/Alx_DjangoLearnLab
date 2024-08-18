# Delete Operation
from bookshelf.models import Book
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(list(books))
