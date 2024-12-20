# Generated by Django 4.2.16 on 2024-11-26 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('FEM', 'Feminismo'), ('ESC', 'Escultura'), ('ABS', 'Abstrato'), ('EMO', 'Emoções'), ('DES', 'Desenho'), ('LIT', 'Literatura'), ('FOT', 'Fotografia'), ('GRA', 'Grafitti')], max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_perfis/')),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('eh_artista', models.BooleanField(default=False)),
                ('interesses', models.ManyToManyField(blank=True, to='usuarios.interesse')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
