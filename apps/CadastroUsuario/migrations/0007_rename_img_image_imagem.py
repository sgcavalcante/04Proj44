# Generated by Django 4.2.6 on 2023-11-20 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroUsuario', '0006_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img',
            new_name='imagem',
        ),
    ]
