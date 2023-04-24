from django.contrib import admin
from user.models import User
from purchase.models import Purchase
from book.models import Book

@admin.register(User)
class User(admin.ModelAdmin):
    fields = ('first_name', 'age')
    list_display = ('id', 'first_name', 'age')
    empty_value_display = 'None'
    ordering = ('id', 'first_name', 'age')
    search_fields = ('first_name',)


@admin.register(Book)
class Book(admin.ModelAdmin):
    fields = ('title', 'author', 'year', 'price')
    list_display = ('id', 'title', 'author', 'year', 'price')
    empty_value_display = 'None'
    ordering = ('id', 'title', 'author', 'year', 'price')
    search_fields = ('id', 'title', 'author', 'year', 'price')


@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    fields = ('user_id', 'book_id')
    list_display = ('id', 'user_id', 'book_id', 'date')
    empty_value_display = 'None'
    ordering = ('id', 'user_id', 'book_id', 'date')
    search_fields = ('id', 'user_id', 'book_id', 'date')

