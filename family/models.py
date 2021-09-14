from django.db import models

# Create your models here.
class Brain(models.Model):
    name=models.CharField(verbose_name='Имя', max_length=255)
    age=models.IntegerField(verbose_name='Возраст')
    about=models.TextField(verbose_name=' О нём')

class Game(models.Model):
    name=models.CharField(verbose_name='Название игры', max_length=255)
    dev=models.CharField(verbose_name='Разработчики игры', max_length=255)
    rel=models.CharField(verbose_name='Дата релиза', max_length=255)
    ser=models.IntegerField(verbose_name='Версия игры')
    gen=models.CharField(verbose_name='Жанр игры', max_length=255)
