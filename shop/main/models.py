from django.db import models


class card(models.Model):
    title = models.CharField('Название Товара', max_length=30)
    description = models.TextField('Описнаие')
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    annotation = models.CharField(max_length=250)

    def get_absolute_url(self):
        return f'/my-ads/{self.id}'

    def __str__(self):
        return self.title

