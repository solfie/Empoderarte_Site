<<<<<<< HEAD
# Generated by Django 4.2.16 on 2024-12-09 23:13
=======
# Generated by Django 5.1.4 on 2024-12-06 16:13
>>>>>>> 498d4e5156a9f6fbc25b2a663bf2642eb762e960

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0003_artista_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='foto',
        ),
    ]
