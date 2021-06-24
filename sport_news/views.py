from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsListSerializer, NewDetailSerializer, CommentCreateSerializer


class NewsListView(APIView):
    """Вывод списка новостей"""
    def get(self, request):
        news = News.objects
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


class NewDetailView(APIView):
    """Вывод новости"""
    def get(self, request, pk):
        new = News.objects.get(id=pk)
        serializer = NewDetailSerializer(new)
        return Response(serializer.data)

class CommentCreateView(APIView):
    """Добавление комментария к новости"""
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)