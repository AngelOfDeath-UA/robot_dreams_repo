from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('<int:id>/', views.OneUser.as_view(), name='user'),
    path('create/', views.CreateUser.as_view(), name='create_user'),
]
