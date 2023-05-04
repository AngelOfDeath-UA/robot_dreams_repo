from django.urls import path
from . import views

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='purchases'),
    path('<int:id>/', views.OnePurchase.as_view(), name='purchase'),
    path('create/', views.CreatePurchase.as_view(), name='create_purchase')

]
