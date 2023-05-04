# from django.http import Http404
# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import PurchaseCreationForm
# from .models import Purchase

from .serializer import PurchaseSerializer
from .models import Purchase
from rest_framework.viewsets import ModelViewSet



# class PurchaseListView(ListView):
#     template_name = 'purchase_list.html'
#     model = Purchase
#
#
# class OnePurchase(DetailView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('id')
#         try:
#             purchase = Purchase.objects.get(id=pk)
#             return render(request, 'one_purchase_view.html', {'purchase': purchase})
#         except Purchase.DoesNotExist:
#             raise Http404(f'Book {pk} not found')
#
#
# class CreatePurchase(CreateView):
#     template_name = 'create.html'
#     model = Purchase
#     form_class = PurchaseCreationForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['url'] = 'create_purchase'
#         return context

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer