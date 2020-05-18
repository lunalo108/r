from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Post
from django.contrib.auth.forms import UserCreationForm
def my_first_view(request):
    return render(
        request,
        'pages/index.html',
        {
            'header':'Index',
            'posts': Post.objects.all()
        
        },
    )

def my_second_view(request):
    return render(
        request,
        'pages/index.html',
        # {
        #     'header':'Index'
        # }
    )


def test_form(request):
    return render(request, 'pages/green.html')  


def contact(request):
    return render(request, 'pages/contact.html')  

    
def graph(request):
    return render(request, 'pages/graph.html')  