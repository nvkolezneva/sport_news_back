# Generated by Django 3.1.4 on 2020-12-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_news', '0002_auto_20201218_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='nameResult',
            field=models.CharField(default='null', max_length=200, verbose_name='Название результатов'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='NameTeam',
            field=models.CharField(max_length=200, verbose_name='Название команды'),
        ),
    ]
