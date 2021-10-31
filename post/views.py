from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from post.serializers import ArticleSerializer
from post.models import Article
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (
        MultiPartParser,
    )