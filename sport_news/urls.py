from django.urls import path

from . import views


urlpatterns = [
path("news/", views.NewsListView.as_view()),
path("news/<int:pk>/", views.NewDetailView.as_view()),
    path("comment/", views.CommentCreateView.as_view())

]