from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            # поиск по названию
            'title': ['icontains'],
            'categoryType': ['icontains'],
        }
