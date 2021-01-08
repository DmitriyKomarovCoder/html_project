from django.db import models
from django.contrib.auth.models import User


class card(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец статьи', blank=True, null=True)
    title = models.CharField('Название Товара', max_length=30)
    phone = models.CharField('Номер телефона', max_length=11, blank=True, null=True)
    description = models.TextField('Описнаие')
    image = models.ImageField(blank=True, null=True, upload_to='images')
    price = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    annotation = models.CharField(max_length=250)


    def get_absolute_url(self):
        return f'/my-ads/{self.id}'

    def __str__(self):
        return self.title

