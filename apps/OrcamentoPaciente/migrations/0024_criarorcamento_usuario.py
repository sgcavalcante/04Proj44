# Generated by Django 4.2.6 on 2023-12-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrcamentoPaciente', '0023_alter_criarorcamento_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='criarorcamento',
            name='usuario',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
