# Generated by Django 4.2 on 2024-06-02 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]