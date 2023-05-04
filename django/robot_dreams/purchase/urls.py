from django.urls import path, include
# from . import views
from rest_framework.routers import SimpleRouter
from .views import PurchaseViewSet

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('', views.PurchaseListView.as_view(), name='purchases'),
#     path('<int:id>/', views.OnePurchase.as_view(), name='purchase'),
#     path('create/', views.CreatePurchase.as_view(), name='create_purchase')
#
# ]

