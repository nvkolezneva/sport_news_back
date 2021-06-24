# Generated by Django 3.1.4 on 2020-12-16 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryNew', models.CharField(max_length=200, verbose_name='Категория новостей')),
            ],
            options={
                'verbose_name': 'Категория новости',
                'verbose_name_plural': 'Категории новости',
            },
        ),
        migrations.CreateModel(
            name='CategoryParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameCategory', models.CharField(max_length=200, verbose_name='Имя категории')),
                ('ageParticipant', models.IntegerField()),
                ('weightParticipant', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Категория участника',
                'verbose_name_plural': 'Категории участников',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameEvent', models.CharField(max_length=200, verbose_name='Мероприятие')),
                ('locationEvent', models.CharField(max_length=200, verbose_name='Место проведения')),
                ('dateEvent', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameRole', models.CharField(max_length=200, verbose_name='Название роли')),
            ],
            options={
                'verbose_name': 'Роль пользователя',
                'verbose_name_plural': 'Роли пользователей',
            },
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameSport', models.TextField(verbose_name='Вид спорта')),
                ('category_participants', models.ManyToManyField(to='sport_news.CategoryParticipants')),
            ],
            options={
                'verbose_name': 'Вид спорта',
                'verbose_name_plural': 'Виды спорта',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('gender', models.CharField(max_length=200, verbose_name='Пол')),
                ('age', models.IntegerField()),
                ('login', models.CharField(max_length=200, verbose_name='Логин')),
                ('password', models.SlugField(unique=True)),
                ('idRole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.roles')),
                ('idSport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.sports')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameTeam', models.TextField(verbose_name='Название команды')),
                ('idSport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.sports')),
                ('idUsers', models.ManyToManyField(to='sport_news.Users')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('idEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.events')),
                ('idTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.teams')),
            ],
            options={
                'verbose_name': 'Результаты соревнований',
                'verbose_name_plural': 'Результаты соревнования',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Новость')),
                ('dateAdd', models.DateField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.categoriesnews')),
                ('idAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.users')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AddField(
            model_name='events',
            name='idNew',
            field=models.ManyToManyField(to='sport_news.News'),
        ),
        migrations.AddField(
            model_name='events',
            name='idSport',
            field=models.ManyToManyField(to='sport_news.Sports'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('dateCommentAdd', models.DateField(auto_now=True)),
                ('idNew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.news')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_news.users')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]