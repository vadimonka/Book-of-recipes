# Generated by Django 3.2.5 on 2021-11-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20211122_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(help_text='Введите название рецепта', max_length=100, verbose_name='Название'),
        ),
    ]
