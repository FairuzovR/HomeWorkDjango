# Generated by Django 5.0.6 on 2024-05-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(
                    max_length=100,
                    verbose_name='заголовок')),
                ('description', models.TextField(
                    max_length=10000,
                    verbose_name='содержимое')),
                ('slug', models.CharField(
                    max_length=150,
                    verbose_name='ссылка')),
                ('images', models.ImageField(
                    blank=True, null=True,
                    upload_to='blog/photo',
                    verbose_name='изображение')),
                ('time_create', models.DateTimeField(
                    auto_now_add=True,
                    null=True,
                    verbose_name='дата создания')),
                ('is_published', models.BooleanField(
                    default=True,
                    verbose_name='опубликовано')),
                ('views_count', models.IntegerField(
                    default=0,
                    verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'заголовоки',
            },
        ),
    ]
