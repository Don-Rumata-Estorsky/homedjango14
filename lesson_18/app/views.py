from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Book, Post

from .forms import *

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context



class CreateBook(CreateView):
    template_name = 'create_book.html'
    model = Book
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('index')

class CreatePost(CreateView):
    template_name = 'create_post.html'
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('index')




class listbooks(ListView):
     model = Book
     template_name = 'library.html'
     context_object_name = 'books'

class listPosts(ListView):
     model = Post
     template_name = 'PostRoom.html'
     context_object_name = 'posts'




class onebook(DetailView):
    model = Book
    template_name = 'onebook.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'

class onePost(DetailView):
    model = Post
    template_name = 'onepost.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'Ppost'




class updatebook(UpdateView):
    model = Book 
    form_class = bookform
    template_name = 'create_book.html'
    success_url = reverse_lazy('index')

    pk_url_kwarg = 'book_id'


class updatePost(UpdateView):
    model = Post 
    form_class = Postform
    template_name = 'create_post.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'post_id'


class detalebook(DetailView):
    model = Book
    template_name = 'detalebook.html'
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'

class detalepost(DetailView):
    model = Post
    template_name = 'detalepost.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'




class deletebook(DeleteView):
    model = Book 
    form_class = bookform
    template_name = 'deletebook.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'

class deletePost(DeleteView):
    model = Post 
    form_class = Postform
    template_name = 'deletepost.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


