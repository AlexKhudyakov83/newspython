# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Author, Post
from datetime import datetime
from pprint import pprint

# class Author(ListView):
#     model = Author
#     ordering = 'name'
#     template_name = 'author.html'
#     context_object_name = 'authors'

class PostList(ListView):
    model = Post
    ordering = 'rating'
    template_name = 'news.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        pprint(context)
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'