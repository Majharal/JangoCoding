from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .models import Post


class ListShowItems(ListView):
    template_name = 'index.html'
    model = Post

class AboutPage(TemplateView):
    template_name = 'about.html'

class CreatePost(CreateView):
    model = Post
    template_name = 'items.html'
    fields = ['title', 'author', 'body']

# Create your views here.
