from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title': 'Leetcode Solutions',
        'author': 'Devang',
        'content': 'DFS',
        'date': 'July 21, 2021'
    },
    {
        'title': 'Football Cup',
        'author': 'Devang Arora',
        'content': 'Copa America',
        'date': 'July 22, 2021'
    }
]


def hello(request):
    # print("Request: ", request.method)
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
