from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryParticipants(models.Model):
    """Категории участников"""
    NameCategory = models.CharField("Имя категории", max_length=200)
    ageParticipant = models.IntegerField(verbose_name="Возраст участников")
    weightParticipant = models.IntegerField(verbose_name="Вес участников")
    def __str__(self):
        return self.NameCategory

    class Meta:
        verbose_name = "Категория участника"
        verbose_name_plural = "Категории участников"

class Roles(models.Model):
    """Роли пользователей"""
    NameRole = models.CharField("Название роли",max_length=200)

    def __str__(self):
        return self.NameRole

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей" 
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Role = models.ForeignKey(
        Roles,
        on_delete=models.CASCADE, verbose_name="Роль"
    )
 
    def __unicode__(self):
        return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
 

class Sports(models.Model):
    """Виды спорта"""
    NameSport = models.TextField("Вид спорта")
    category_participants = models.ManyToManyField(
        CategoryParticipants,verbose_name="Категории участников"
    )
    def __str__(self):
        return self.NameSport

    class Meta:
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"

class Users(models.Model):
    """Пользователи"""
    name = models.CharField("Имя", max_length=200)
    gender = models.CharField("Пол", max_length=200)
    age = models.IntegerField(verbose_name="Возраст")
    login = models.CharField("Логин", max_length=200)
    password = models.SlugField(max_length=50, unique=True)
    Sport = models.ForeignKey(
        Sports,
        on_delete=models.CASCADE, verbose_name="Вид спорта"
    )
    Role = models.ForeignKey(
        Roles,
        on_delete=models.CASCADE, verbose_name="Роль"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class CategoriesNews(models.Model):
    """Категории новостей"""
    CategoryNew = models.CharField("Категория новостей",max_length=200)

    def __str__(self):
        return self.CategoryNew

    class Meta:
        verbose_name = "Категория новости"
        verbose_name_plural = "Категории новостей"

class News(models.Model):
    """Новости"""
    Author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,verbose_name="Автор"
    )
    body = models.TextField("Новость")
    dateAdd = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Дата создания")
    PublishedOrNot = models.BooleanField(default=False, verbose_name="Публикация")
    categories = models.ForeignKey(
        CategoriesNews,
        on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Comments(models.Model):
    """Комментарии"""
    User = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,verbose_name="Автор"
    )
    New = models.ForeignKey(
        News,
        on_delete=models.CASCADE, verbose_name="Новости", related_name="comments"

    )
    text = models.TextField("Текст комментария")
    dateCommentAdd = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Дата создания")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Events(models.Model):
    """Мероприятия"""
    nameEvent = models.CharField("Мероприятие", max_length=200)
    locationEvent = models.CharField("Место проведения", max_length=200)
    dateEvent = models.DateField(verbose_name="Дата проведения")
    DoneOrNot = models.BooleanField(default=False, verbose_name="Проведение")
    Sport = models.ManyToManyField(
        Sports, verbose_name="Вид спорта"
    )
    New = models.ManyToManyField(
        News, verbose_name="Новость о мероприятие"
    )
    

    def __str__(self):
        return self.nameEvent

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

class Teams(models.Model):
    """Команды участников"""
    NameTeam = models.CharField("Название команды", max_length=200)
    Users = models.ManyToManyField(
        Users, verbose_name="Участник команды"
    )
    Sport = models.ForeignKey(
        Sports,
        on_delete=models.CASCADE, verbose_name="Вид спорта"
    )
    def __str__(self):
        return self.NameTeam

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class Results(models.Model):
    """Результаты соревнований"""
    nameResult = models.CharField("Название результатов", max_length=200,default="null")
    points = models.IntegerField(verbose_name="Баллы")
    Event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE, verbose_name="Мероприятие"
    )
    Team = models.ForeignKey(
        Teams,
        on_delete=models.CASCADE, verbose_name="Команда"
    )
    def __str__(self):
        return self.nameResult

    class Meta:
        verbose_name = "Результаты соревнований"
        verbose_name_plural = "Результаты соревнования"     
