# Generated by Django 4.2.2 on 2023-06-19 13:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autor',
            new_name='Author',
        ),
    ]
