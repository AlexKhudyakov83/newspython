from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'categoryType')
    list_filter = ('title', 'rating')
    search_fields = ('rating',)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
