# Generated by Django 4.0.4 on 2022-04-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_portfolio_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='skills',
            field=models.TextField(blank=True, max_length=500, verbose_name='Навыки'),
        ),
    ]
