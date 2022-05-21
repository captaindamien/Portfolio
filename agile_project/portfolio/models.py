from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'user_avatars/user_{0}/{1}'.format(instance.username.id, filename)

class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField(blank=True, verbose_name="Обратная связь")
    is_readed = models.BooleanField(default=False, verbose_name="Прочитано")

    def __str__(self):

        return f'отзыв_{self.id}'

class Portfolio(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    career = models.CharField(
        verbose_name='Род деятельности',
        blank=False,
        max_length=64,
        choices=[
            ('Программист', 'Программист'),
            ('Дизайнер', 'Дизайнер'),
            ('Специалист', 'Специалист'),
        ],
        default="Специалист",
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
        blank=False,
        choices=[
            ('Нет опыта', 'Нет опыта'),
            ('От 1 года до 3 лет', 'От 1 года до 3 лет'),
            ('От 3 до 6 лет ', 'От 3 до 6 лет '),
            ('Более 6 лет', 'Более 6 лет'),
        ],
        default="Нет опыта",
    )
    skills = models.TextField(
        verbose_name='Навыки',
        blank=True,
        max_length=200,
    )
    template = models.CharField(
        blank=False,
        max_length=1,
        verbose_name='Выбор шаблона',
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        ],
        default=1,
    )

    def __str__(self):
        return str(self.username)
