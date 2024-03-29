# Generated by Django 4.0.4 on 2022-04-14 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(blank=True, max_length=100, verbose_name='Род деятельности')),
                ('photo', models.ImageField(blank=True, upload_to=portfolio.models.user_directory_path, verbose_name='Фото')),
                ('about_me', models.TextField(blank=True, verbose_name='Информация о себе')),
                ('project_links', models.TextField(blank=True, verbose_name='Ссылки на проекты')),
                ('telegram', models.CharField(blank=True, max_length=100, verbose_name='Ссылка на telegram')),
                ('whatsapp', models.CharField(blank=True, max_length=100, verbose_name='Ссылкa на whatsapp')),
                ('phone_number', models.CharField(blank=True, max_length=100, verbose_name='Номер телефона')),
                ('experience', models.CharField(blank=True, max_length=100, verbose_name='Опыт работы')),
                ('skills', models.TextField(blank=True, verbose_name='Навыки')),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
