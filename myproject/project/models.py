from urllib import request

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.utils.crypto import get_random_string


class User(AbstractUser):
    fname = models.CharField(max_length=150, verbose_name='Имя', null=False, blank=False)
    lname = models.CharField(max_length=150, verbose_name='Фамилия', null=True, blank=False)
    sname = models.CharField(max_length=150, verbose_name='Отчество', null=False, blank=False)
    username = models.CharField(max_length=150, verbose_name='Никнейм', unique=True, null=False, blank=False)
    email = models.CharField(max_length=250, verbose_name='Почта', unique=False, null=False, blank=False)
    password = models.CharField(max_length=250, verbose_name='Пароль', null=False, blank=False)
    personal_data = models.BooleanField(default=False, blank=False, null=False,
                                        verbose_name='Согласие на обработку персональных данных')



def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


def validate_image_size(img):
    filesize = img.file.size
    megabyte_max = 2.0
    if filesize > megabyte_max * 1024 * 1024:
        raise ValidationError("Максимальный размер %sMB" % str(megabyte_max))



class Aplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    name = models.CharField(max_length=250, verbose_name='Имя', null=False, blank=True)
    description = models.CharField(max_length=250, verbose_name='Описание', null=False, blank=True)
    Category = models.ForeignKey('project.Category', verbose_name='Категория', blank=False, null=False,
                                 on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_name_file, blank=False,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp']),
                                          validate_image_size])
    date = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)
    status_choices = [
        ('new', 'Новая'),
        ('received', 'В обработке'),
        ('done', 'Выполнено')
    ]
    status = models.CharField(max_length=250, verbose_name='Статус', choices=status_choices, default='new')
    comment = models.CharField(max_length=250, verbose_name='Комментарий', blank=True)
    second_photo = models.ImageField(upload_to=get_name_file, blank=False,
                                     validators=[
                                         FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp']),
                                         validate_image_size], null=True)

    def status_verbose(self):
        return dict(self.status_choices)[self.status]



    def __str__(self):
        return str(self.name) + ' | ' + str(self.Category) + ' | ' + str(self.status_verbose())



    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложение"

class Category(models.Model):
    name = models.CharField(max_length=250,
                            null=False,
                            blank=False)


    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
