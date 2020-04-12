from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def my_first_view(request):
    return render(
        request,
        'pages/index.html',
        {
            'header':'Index',
            'posts': Post.objects.all()
        
        }
    )

def my_second_view(request):
    return render(
        request,
        'pages/index.html',
        {
            'header':'Index'
        }
    )

