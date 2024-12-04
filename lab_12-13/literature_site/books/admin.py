from django.contrib import admin
from .models import Author, Genre, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date')
    list_filter = ('author', 'genre')

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
