from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# Create New post and retrive all existing post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Crud method perform on post
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer