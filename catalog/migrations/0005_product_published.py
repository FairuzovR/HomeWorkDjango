# Generated by Django 4.2 on 2024-06-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published',
            field=models.BooleanField(
                default=False,
                verbose_name='Опубликован'),
        ),
    ]
