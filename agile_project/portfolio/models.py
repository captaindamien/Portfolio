from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def user_directory_path(instance, filename):
    return 'user_avatars/user_{0}/{1}'.format(instance.full_name.id, filename)


class Portfolio(models.Model):
    full_name = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    career = models.CharField(
        verbose_name='Род деятельности',
        max_length=100,
        blank=True,
    )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to=user_directory_path,
        blank=True,
    )
    about_me = models.TextField(
        verbose_name='Информация о себе',
        blank=True,
    )
    project_links = models.TextField(
        verbose_name='Ссылки на проекты',
        blank=True,
    )
    telegram = models.CharField(
        verbose_name='Ссылка на telegram',
        max_length=100,
        blank=True,
    )
    whatsapp = models.CharField(
        verbose_name='Ссылкa на whatsapp',
        max_length=100,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        max_length=100,
        blank=True,
    )
    experience = models.CharField(
        verbose_name='Опыт работы',
        max_length=100,
        blank=True,
    )
    skills = models.TextField(
        verbose_name='Навыки',
        blank=True,
    )
