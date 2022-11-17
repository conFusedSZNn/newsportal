from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AuthorUser, Category, Post, PostCategory, Comment


class PostList(ListView):
    model = Post
    ordering = 'one_to_many_post'
    template_name = 'nwsportal.html'
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    pk_url_kwarg = 'id'
