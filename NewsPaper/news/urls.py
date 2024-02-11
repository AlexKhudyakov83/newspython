from django.urls import path
from .views import PostList, PostDetail, PostCreate, \
   PostUpdate, PostDelete, PostSearch, PostCreateArticle, PostUpdateArticle, PostDeleteArticle


urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('articles/create/', PostCreateArticle.as_view(), name='post_article_create'),
   path('articles/<int:pk>/update/', PostUpdateArticle.as_view(), name='post_article_update'),
   path('articles/<int:pk>/delete/', PostDeleteArticle.as_view(), name='post_article_update'),
]
