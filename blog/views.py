from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.
class BlogsListView(ListView): # представление в виде списка
    model = Blog                   # модель для представления

class BlogDetailView(DetailView): # детализированное представление модели
    model = Blog

# def blog(request):
#     blogs = Blog.objects.all()
#     return render(request, 'landing/blog.html', locals())
