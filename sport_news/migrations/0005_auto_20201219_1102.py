# Generated by Django 3.1.4 on 2020-12-19 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_news', '0004_auto_20201219_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='idNew',
            new_name='New',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='idUser',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='idNew',
            new_name='New',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='idSport',
            new_name='Sport',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='idAuthor',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='idEvent',
            new_name='Event',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='idTeam',
            new_name='Team',
        ),
        migrations.RenameField(
            model_name='teams',
            old_name='idSport',
            new_name='Sport',
        ),
        migrations.RenameField(
            model_name='teams',
            old_name='idUsers',
            new_name='Users',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='idRole',
            new_name='Role',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='idSport',
            new_name='Sport',
        ),
    ]