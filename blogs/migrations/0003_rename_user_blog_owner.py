# Generated by Django 4.2 on 2024-06-02 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='owner',
        ),
    ]
