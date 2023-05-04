# from django.http import Http404
# from .models import Book
# from django.views.generic import ListView, DetailView, CreateView
# from django.shortcuts import render
# from .forms import BookCreationForm

from .serializer import BookSerializer
from .models import Book
from rest_framework.viewsets import ModelViewSet

# class BookListView(ListView):
#     template_name = 'book_list.html'
#     model = Book
#
#
# class OneBook(DetailView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('id')
#         try:
#             book = Book.objects.get(id=pk)
#             return render(request, 'one_book_view.html', {'book': book})
#         except Book.DoesNotExist:
#             raise Http404(f'Book {pk} not found')
#
#
# class CreateBook(CreateView):
#     template_name = 'create.html'
#     model = Book
#     form_class = BookCreationForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['url'] = 'create_book'
#         return context

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer