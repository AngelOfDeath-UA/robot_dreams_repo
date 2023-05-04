from django.urls import path, include
# from . import views
from rest_framework.routers import SimpleRouter
from .views import BookViewSet

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('', views.BookListView.as_view(), name='books'),
#     path('<int:id>/', views.OneBook.as_view(), name='book'),
#     path('create/', views.CreateBook.as_view(), name='create_book')
#
# ]
