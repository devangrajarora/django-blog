from restapi import serializers
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer
from .models import Blog

@api_view(['GET'])
def hello(request):
    details = {
        'name': 'Devang',
        'age': 21,
        'interests': ['UFC', 'Football', 'Chess'] 
    }

    return Response(details)

@api_view(['GET'])
def view_blog(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_detail(request,pk):
    blogs = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blogs)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)