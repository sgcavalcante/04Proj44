# Generated by Django 4.2.6 on 2024-01-01 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrcamentoPaciente', '0033_alter_criarorcamento_numero_orcamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criarorcamento',
            old_name='numero_orcamento',
            new_name='numero_orcamento1',
        ),
    ]
