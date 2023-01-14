from django.contrib import admin
from .models import AuthorUser, Category, Post, PostCategory, Comment


admin.site.register(AuthorUser)
admin.site.register(Category)
admin.site.register( Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
