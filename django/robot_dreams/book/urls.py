from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('<int:id>/', views.OneBook.as_view(), name='book'),
    path('create/', views.CreateBook.as_view(), name='create_book')

]
