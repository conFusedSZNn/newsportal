from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm



class PostList(ListView):
    model = Post
    ordering = 'one_to_many_post'
    template_name = 'nwsportal.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class SearchList(ListView):
    model = Post
    ordering = 'one_to_many_post'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10
    
class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.chs = 2
        return super().form_valid(form)

class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.chs = 2
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.chs = 2
        return super().form_valid(form)

class PostartCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.chs = 1
        return super().form_valid(form)

class PostartEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.chs = 1
        return super().form_valid(form)

class PostartDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.chs = 1
        return super().form_valid(form)
