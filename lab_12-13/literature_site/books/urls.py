from django.urls import path
from .views import home
from .views import book_detail
from .views import add_book
from .views import edit_book

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
]



