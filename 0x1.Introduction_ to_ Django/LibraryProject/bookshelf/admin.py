from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

# Register the Book model
admin.site.register(Book)

# Custom admin class for Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in list view
    list_filter = ('author', 'publication_year')  # Fields to filter the list by
    search_fields = ('title', 'author')  # Fields to search by

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
