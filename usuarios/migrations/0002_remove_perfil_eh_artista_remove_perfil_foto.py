# Generated by Django 4.2.16 on 2024-12-03 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='eh_artista',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='foto',
        ),
    ]
