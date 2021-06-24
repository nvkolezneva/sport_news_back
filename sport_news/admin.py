from django.contrib import admin
from .models import News, CategoriesNews, Comments, Events, CategoryParticipants, Teams, Sports, Results, Roles, Users,UserProfile
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'
 
# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

class CommentsInline(admin.TabularInline):
    """Отзывы на странице новости"""
    model = Comments
    extra = 1
class NewsAdmin(ImportExportActionModelAdmin):
    pass
class CategoriesNewsAdmin(ImportExportActionModelAdmin):
    pass
class CommentsAdmin(ImportExportActionModelAdmin):
    pass
class EventsAdmin(ImportExportActionModelAdmin):
    pass
class CategoryParticipantsAdmin(ImportExportActionModelAdmin):
    pass
class TeamsAdmin(ImportExportActionModelAdmin):
    pass
class SportsAdmin(ImportExportActionModelAdmin):
    pass
class ResultsAdmin(ImportExportActionModelAdmin):
    pass
class UsersAdmin(ImportExportActionModelAdmin):
    pass

class NewsResource(resources.ModelResource):

    class Meta:
        model = News
        skip_unchanged = True
        report_skipped = False
        widgets = {
                'dateAdd': {'format': '%d.%m.%Y'},
                }
        fields = ("Author", "dateAdd", "categories","body","PublishedOrNot","comments")
    
    def dehydrate_full_title(self, new):
        return '%s by %s' % (new.body, new.Author.name)

class NewsAdmin(ImportExportModelAdmin):
    """Новости"""
    list_display = ("id", "Author", "body", "dateAdd", "categories", "PublishedOrNot")
    list_display_links = ("body",)
    list_filter = ("Author",)
    search_fields = ("Author__name",)
    inlines=[CommentsInline]
    save_on_top = True
    save_as = True
    list_editable= ("categories","PublishedOrNot")
    actions = ["published", "unpublished"]

    def unpublished(self, request,queryset):
        """Снять с публикации"""
        row_update = queryset.update(PublishedOrNot=False)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    def published(self, request,queryset):
        """Опубликовать"""
        row_update = queryset.update(PublishedOrNot=True)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    published.short_description = "Опубликовать"
    published.allowed_permissions = ('change',)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ('change',)
    resource_class = NewsResource


class CategoriesNewsResource(resources.ModelResource):

    class Meta:
        model = CategoriesNews
        skip_unchanged = True
        report_skipped = False
        fields = ("CategoryNew",)

class CategoriesNewsAdmin(ImportExportModelAdmin):
    """Категории новостей"""
    list_display = ("id", "CategoryNew")
    list_display_links = ("CategoryNew",)
    search_fields = ("CategoryNew",)
    resource_class = CategoriesNewsResource

class CommentsResource(resources.ModelResource):

    class Meta:
        model = Comments
        skip_unchanged = True
        report_skipped = False
        widgets = {
                'dateCommentAdd': {'format': '%d.%m.%Y'},
                }
        fields = ("User", "New", "text","dateCommentAdd")
    
    def dehydrate_full_title(self, comment):
        return '%s by %s' % (comment.text, comment.User.name)

class CommentsAdmin(ImportExportModelAdmin):
    """Комментарии"""
    list_display = ("id", "User","New","text","dateCommentAdd")
    list_display_links = ("text",)
    list_filter = ("User",)
    search_fields = ("User__name",)
    resource_class = CommentsResource

    
class EventsResource(resources.ModelResource):

    class Meta:
        model = Events
        skip_unchanged = True
        report_skipped = False
        widgets = {
                'dateEvent': {'format': '%d.%m.%Y'},
                }
        fields = ("nameEvent", "locationEvent", "dateEvent","DoneOrNot","Sport","New")

class EventsAdmin(ImportExportModelAdmin):
    """Мероприятия"""
    list_display = ("id", "nameEvent","locationEvent","dateEvent", "DoneOrNot")
    list_display_links = ("nameEvent",)
    list_filter = ("nameEvent",)
    search_fields = ("nameEvent",)
    actions = ["notdone", "done"]
    list_editable= ("DoneOrNot",)
    def notdone(self, request,queryset):
        """Отметка о непроведении мероприятия"""
        row_update = queryset.update(DoneOrNot=False)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    def done(self, request,queryset):
        """Отметка о проведении мероприятия"""
        row_update = queryset.update(DoneOrNot=True)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    done.short_description = "Провести мероприятие"
    done.allowed_permissions = ('change',)

    notdone.short_description = "Не проводить мероприятие"
    notdone.allowed_permissions = ('change',)
    resource_class = EventsResource


class CategoryParticipantsResource(resources.ModelResource):

    class Meta:
        model = CategoryParticipants
        skip_unchanged = True
        report_skipped = False
        fields = ("NameCategory", "ageParticipant", "weightParticipant")

class CategoryParticipantsAdmin(ImportExportModelAdmin):
    """Категории участников"""
    list_display = ("id", "NameCategory","ageParticipant","weightParticipant")
    list_display_links = ("NameCategory",)
    list_filter = ("NameCategory",)
    search_fields = ("NameCategory",)
    resource_class = CategoryParticipantsResource


class TeamsResource(resources.ModelResource):

    class Meta:
        model = Teams
        skip_unchanged = True
        report_skipped = False
        fields = ("NameTeam", "Users", "Sport")

class TeamsAdmin(ImportExportModelAdmin):
    """Команды"""
    list_display = ("id", "NameTeam","Sport")
    list_display_links = ("NameTeam",)
    list_filter = ("NameTeam",)
    search_fields = ("NameTeam",)
    resource_class = TeamsResource

class SportsResource(resources.ModelResource):

    class Meta:
        model = Sports
        skip_unchanged = True
        report_skipped = False
        fields = ("NameSport", "category_participants")

class SportsAdmin(ImportExportModelAdmin):
    """Виды спорта"""
    list_display = ("id", "NameSport")
    list_display_links = ("NameSport",)
    search_fields = ("NameSport",)
    resource_class = SportsResource

class ResultsResource(resources.ModelResource):

    class Meta:
        model = Results
        skip_unchanged = True
        report_skipped = False
        fields = ("nameResult", "points","Event","Team")

class ResultsAdmin(ImportExportModelAdmin):
    """Результаты"""
    list_display = ("id", "nameResult","points","Event", "Team")
    list_display_links = ("nameResult",)
    list_filter = ("nameResult",)
    search_fields = ("points",)
    resource_class = ResultsResource

class RolesResource(resources.ModelResource):

    class Meta:
        model = Roles
        skip_unchanged = True
        report_skipped = False
        fields = ("NameRole")

class RolesAdmin(ImportExportModelAdmin):
    """Роли пользователей"""
    list_display = ("id", "NameRole")
    list_display_links = ("NameRole",)
    search_fields = ("NameRole",)
    resource_class = RolesResource

class UsersResource(resources.ModelResource):
    class Meta:
        model = Users
        skip_unchanged = True
        report_skipped = False
        fields = ("name","gender","age","login","password","Sport","Role")
        

class UsersAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "gender", "age", "login", "Sport", "Role" )
    list_display_links = ("name",)
    list_filter = ("age",)
    search_fields = ("name",)
    readonly_fields = ("login","password")
    resource_class = UsersResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CategoriesNews, CategoriesNewsAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(CategoryParticipants, CategoryParticipantsAdmin)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Sports, SportsAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Users, UsersAdmin)
# Register your models here.
