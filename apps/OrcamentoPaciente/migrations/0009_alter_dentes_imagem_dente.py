# Generated by Django 4.2.6 on 2023-12-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrcamentoPaciente', '0008_remove_orcamento_procedimentos_dentes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentes',
            name='imagem_dente',
            field=models.ImageField(default=None, upload_to='Odontograma/'),
        ),
    ]