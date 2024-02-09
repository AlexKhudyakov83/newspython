# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView,\
    CreateView, UpdateView, DeleteView
from .models import Author, Post
from datetime import datetime
from pprint import pprint
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy



class Author(ListView):
    model = Author
    ordering = 'name'
    template_name = 'author.html'
    context_object_name = 'authors'


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()
    #     context['next_news'] = None
    #     context['filterset'] = self.filterset
    #     pprint(context)
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class PostSearch(ListView):
    form_class = PostFilter
    model = Post
    template_name = 'post_search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = None
        context['filterset'] = self.filterset
        pprint(context)
        return context

