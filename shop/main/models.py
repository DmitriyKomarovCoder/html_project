from django.db import models

class card(models.Model):
    title = models.CharField('Название Товара', max_length=15)
    description = models.TextField('Описнаие')

    def __str__(self):
        return self.title