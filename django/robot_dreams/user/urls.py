from django.urls import path, include
# from . import views
from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', views.UserListView.as_view(), name='users'),
    # path('<int:id>/', views.OneUser.as_view(), name='user'),
    # path('create/', views.CreateUser.as_view(), name='create_user'),
]
