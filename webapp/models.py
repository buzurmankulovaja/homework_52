from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Task(models.Model):
    description = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Описание'
    )

    detailed_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Подробное описание'
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='new',
        verbose_name='Статус'
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата выполнения'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.id}- {self.description}'


