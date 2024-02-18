# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView,\
    CreateView, UpdateView, DeleteView
from .models import Author, Post
from datetime import datetime
from pprint import pprint
from .filters import PostFilter
from .forms import PostForm, PostFormArticle
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


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


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.post_create',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostCreateArticle(PermissionRequiredMixin, CreateView):
    permission_required = ('news.post_article_create',)
    form_class = PostFormArticle
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'Статья'
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.post_update',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdateArticle(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.post_article_update',)
    form_class = PostFormArticle
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'Статья'
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostDeleteArticle(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'Статья'
        return super().form_valid(form)


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

