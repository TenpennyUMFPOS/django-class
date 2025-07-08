from django.contrib import admin
from .models import Author, Category, Tag, Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('created_at', 'author', 'category')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('name', 'email', 'content')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
