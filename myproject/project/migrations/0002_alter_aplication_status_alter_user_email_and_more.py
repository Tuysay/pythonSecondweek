# Generated by Django 4.2.7 on 2023-11-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplication',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('received', 'В обработке'), ('done', 'Выполнено')], default='new', max_length=250, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=250, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Никнейм'),
        ),
    ]
