from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


class GenericArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
