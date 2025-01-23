from django.views.generic import ListView

from .models import Books


class BookListView(ListView):
    model = Books
    context_object_name = "book_list"
    template_name = "books/book_list.html"
