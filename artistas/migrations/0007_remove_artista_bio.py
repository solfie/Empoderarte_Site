# Generated by Django 5.1.4 on 2024-12-06 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0006_remove_artista_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='bio',
        ),
    ]
