from django.db import models
from django.conf import settings
import random


class Link(models.Model):
    original_link = models.URLField('Оригинальная ссылка')
    code = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return f'Ссылка: {self.code}'

    def save(self, *args, **kwargs):
        self.code = ''.join([random.choice(settings.CODE_CHAR)
                             for i in range(15)])
        super(Link, self).save(*args, **kwargs)
