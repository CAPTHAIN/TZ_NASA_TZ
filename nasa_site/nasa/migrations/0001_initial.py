# Generated by Django 3.2.8 on 2021-10-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('text', models.TextField(verbose_name='Опис')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
                'ordering': ['title', 'date'],
            },
        ),
    ]
