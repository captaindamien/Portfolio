# Generated by Django 4.0.4 on 2022-04-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_full_name_portfolio_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='template',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Выбор шаблона'),
        ),
    ]
