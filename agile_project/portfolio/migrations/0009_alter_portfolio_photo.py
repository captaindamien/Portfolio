# Generated by Django 4.0.4 on 2022-04-14 20:40

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_portfolio_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='photo',
            field=models.ImageField(blank=True, upload_to=portfolio.models.user_directory_path, verbose_name='Фото'),
        ),
    ]
