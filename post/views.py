from django.shortcuts import render
from rest_framework import viewsets
from post.serializers import ArticleSerializer
from post.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer