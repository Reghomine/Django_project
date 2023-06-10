from typing import Any
from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задача'