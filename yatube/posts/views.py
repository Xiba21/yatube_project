from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    context = {
        'title': 'Блог о книшшках',
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context)
	
	
def group_posts(request, slug):
    template = 'posts/group_posts.html'
    context = {
        'title': 'Группы',
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context) 	