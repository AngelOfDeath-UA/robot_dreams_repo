# from django.http import Http404
# from .forms import UserCreationForm
#
# from django.views.generic import ListView, DetailView, CreateView
# from django.shortcuts import render

from .serializer import UserSerializer
from .models import User
from rest_framework.viewsets import ModelViewSet
from .pagination import CustomPaginator


# class UserListView(ListView):
#     template_name = 'user_list.html'
#     model = User
#
#
# class OneUser(DetailView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('id')
#         try:
#             user = User.objects.get(id=pk)
#             return render(request, 'one_user_view.html', {'user': user})
#         except User.DoesNotExist:
#             raise Http404(f'Book {pk} not found')
#
#
# class CreateUser(CreateView):
#     template_name = 'create.html'
#     model = User
#     form_class = UserCreationForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['url'] = 'create_user'
#         return context

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator
    search_fields = ["first_name", "age"]
    ordering_fields = ["first_name", "age"]
