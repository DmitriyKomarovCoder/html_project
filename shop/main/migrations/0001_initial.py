# Generated by Django 3.1.4 on 2021-01-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='Название Товара')),
                ('description', models.TextField(verbose_name='Описнаие')),


            ],
        ),
    ]
