from django.conf import settings
from graphene_django import DjangoObjectType

from sport_news import models
import graphene

# class UserType(DjangoObjectType):
#     class Meta:
#         model = settings.AUTH_USER_MODEL

class CategoryParticipantsType(DjangoObjectType):
    class Meta:
        model = models.CategoryParticipants

class RolesType(DjangoObjectType):
    class Meta:
        model = models.Roles

class UserProfileType(DjangoObjectType):
    class Meta:
        model = models.UserProfile

class SportsType(DjangoObjectType):
    class Meta:
        model = models.Sports

class UsersType(DjangoObjectType):
    class Meta:
        model = models.Users

class CategoriesNewsType(DjangoObjectType):
    class Meta:
        model = models.CategoriesNews

class NewsType(DjangoObjectType):
    class Meta:
        model = models.News

class CommentsType(DjangoObjectType):
    class Meta:
        model = models.Comments

class EventsType(DjangoObjectType):
    class Meta:
        model = models.Events

class TeamsType(DjangoObjectType):
    class Meta:
        model = models.Teams

class ResultsType(DjangoObjectType):
    class Meta:
        model = models.Results

class Query(graphene.ObjectType):
    all_news = graphene.List(NewsType)
    all_events = graphene.List(EventsType)
    all_comments_for_one_news = graphene.Field(CommentsType, New_id=graphene.ID())
    one_news = graphene.Field(NewsType, id=graphene.ID())
    one_event = graphene.Field(EventsType, id=graphene.ID())
    all_teams = graphene.List(TeamsType)
    all_results = graphene.List(ResultsType)

    # author_by_username = graphene.Field(AuthorType, username=graphene.String())
    # post_by_slug = graphene.Field(PostType, slug=graphene.String())
    # posts_by_author = graphene.List(PostType, username=graphene.String())
    # posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_news(root, info):
        return (
            models.News.objects
            .select_related("Author","categories")
            .all()
        )
        
    def resolve_all_events(root, info):
        return (
            models.Events.objects.prefetch_related("Sport","New")
            .all()
        )
    def resolve_all_comments_for_one_news(root, info,New_id):
        return (
            models.Comments.objects.get(pk=New_id)
        )
    def resolve_all_teams(root, info):
        return (
            models.Teams.objects
            .select_related("Sport").prefetch_related("Users")
            .all()
        )
    def resolve_all_results(root, info):
        return (
            models.Results.objects
            .select_related("Author","categories")
            .all()
        )
    def resolve_one_news(root, info,id):
        return (
            models.News.objects.get(pk=id)
        )
    def resolve_one_event(root, info,id):
        return (
            models.Events.objects.get(pk=id)
        )
class CommentInput(graphene.InputObjectType):
    text = graphene.String(required=True)
    New_id = graphene.ID(required=True)
    User_id = graphene.ID(required=True)

class CreateComment(graphene.Mutation):
    class Arguments:
        comment_data = CommentInput(required=True)

    comment = graphene.Field(CommentsType)

    def mutate(root, info, comment_data=None):
        comment = CommentsType(
            text=comment_data.text,
            New=models.News.objects.get(pk=comment_data.New_id),
            User=models.Users.objects.get(pk=comment_data.User_id)
        )
        return CreateComment(comment=comment)


class DeleteComment(graphene.Mutation):
    class Arguments:
        comment_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, comment_id):
        comment = models.Comments.objects.get(pk=comment_id)
        comment.delete()

        return cls(ok=True)




class MyMutations(graphene.ObjectType):
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)
    # def resolve_author_by_username(root, info, username):
    #     return models.Profile.objects.select_related("user").get(
    #         user__username=username
    #     )

    # def resolve_post_by_slug(root, info, slug):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .get(slug=slug)
    #     )

    # def resolve_posts_by_author(root, info, username):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .filter(author__user__username=username)
    #     )

    # def resolve_posts_by_tag(root, info, tag):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .filter(tags__name__iexact=tag)
    #     )