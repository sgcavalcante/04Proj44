# Generated by Django 4.2.6 on 2023-12-23 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrcamentoPaciente', '0027_rename_procedimento_criarorcamento_procedimentos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criarorcamento',
            old_name='procedimentos',
            new_name='procedimento',
        ),
    ]
