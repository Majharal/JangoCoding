from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post


class ListShowItems(ListView):
    template_name = 'index.html'
    model = Post

class AboutPage(TemplateView):
    template_name = 'about.html'

# Create your views here.
