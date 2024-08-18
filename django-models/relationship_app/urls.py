from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import user_login
from .views import user_logout
from .views import user_register
from .views import admin_view
from .views import librarian_view
from .views import member_view
urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    "views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="
]
