from django.contrib import admin
from user.models import User
from purchase.models import Purchase
from book.models import Book

admin.site.register(User)
admin.site.register(Purchase)
admin.site.register(Book)
