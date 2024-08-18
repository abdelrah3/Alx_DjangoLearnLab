from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import user_login
from .views import user_logout
from .views import user_register
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import add_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('books/add/', add_book_view, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book_view, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book_view, name='delete_book'),
    "views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
    "add_book/", "edit_book"
]
