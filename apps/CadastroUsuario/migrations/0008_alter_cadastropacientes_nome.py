# Generated by Django 4.2.6 on 2023-11-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroUsuario', '0007_rename_img_image_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastropacientes',
            name='nome',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
