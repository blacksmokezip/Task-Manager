from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status
from django.contrib.auth.models import User


class Task(models.Model):

    name = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
        verbose_name='Имя'
    )
    description = models.TextField(
        max_length=10000,
        blank=True,
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Автор'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='statuses',
        verbose_name='Статус'
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        verbose_name='Исполнитель'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
