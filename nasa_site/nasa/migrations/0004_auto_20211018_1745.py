# Generated by Django 3.2.8 on 2021-10-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasa', '0003_auto_20211018_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date', 'title'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.FileField(blank=True, upload_to='db_photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]