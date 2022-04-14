# Generated by Django 4.0.4 on 2022-04-14 19:59

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(blank=True, default='/media/person_logo.png', upload_to=portfolio.models.user_directory_path, verbose_name='Фото'),
        ),
    ]
