from rest_framework import serializers
from .models import Comments, News


class NewsListSerializer(serializers.ModelSerializer):
    """Список новостей"""

    class Meta:
        model = News
        fields = ("id","dateAdd", "categories")

class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""

    class Meta:
        model = Comments
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""
    User = serializers.SlugRelatedField(slug_field="name", read_only=True)
    New = serializers.SlugRelatedField(slug_field="body", read_only=True)

    class Meta:
        model = Comments
        fields = ("User", "New", "text","dateCommentAdd")

class NewDetailSerializer(serializers.ModelSerializer):
    """Полная новость"""
    Author = serializers.SlugRelatedField(slug_field="name", read_only=True)
    categories = serializers.SlugRelatedField(slug_field="CategoryNew", read_only=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = News
        fields = ("Author", "dateAdd", "categories","body","PublishedOrNot","comments")