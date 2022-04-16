# Generated by Django 4.0.4 on 2022-04-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_portfolio_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='template',
            field=models.CharField(choices=[('1', 'radio-1'), ('2', 'radio-2')], default=1, max_length=1, verbose_name='Выбор шаблона'),
        ),
    ]
