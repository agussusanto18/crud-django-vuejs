from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions
from post.serializers import ArticleSerializer
from django.forms.models import model_to_dict
from post.models import Article
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    UpdateModelMixin, 
    CreateModelMixin, 
    DestroyModelMixin, 
    ListModelMixin, 
    RetrieveModelMixin
)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (
        MultiPartParser,
    )

    # def update(self, request, *args, **kwargs):
    #     print('**************************************************')
    #     partial = kwargs.pop('partial', True)
    #     instance = self.get_object()

    #     datadict = model_to_dict(instance)
    #     print(datadict)
    #     print(request.data)
        
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)

# class ArticleViewSet(
#     GenericAPIView, 
#     UpdateModelMixin, 
#     CreateModelMixin, 
#     DestroyModelMixin, 
#     ListModelMixin, 
#     RetrieveModelMixin
# ):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     parser_classes = (
#         MultiPartParser,
#     )

#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)