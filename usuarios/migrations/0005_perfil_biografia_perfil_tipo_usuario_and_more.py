# Generated by Django 5.1.4 on 2024-12-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_perfil_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.CharField(choices=[('comum', 'Usuário Comum'), ('artista', 'Artista')], default='comum', max_length=10),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfil_fotos/'),
        ),
    ]
