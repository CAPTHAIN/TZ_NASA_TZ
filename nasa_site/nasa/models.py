from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    photo = models.FileField(upload_to="db_photos", verbose_name='Фото', blank=True)
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date', 'title']