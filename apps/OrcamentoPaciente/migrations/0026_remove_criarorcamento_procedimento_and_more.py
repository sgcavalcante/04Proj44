# Generated by Django 4.2.6 on 2023-12-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrcamentoPaciente', '0025_alter_criarorcamento_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criarorcamento',
            name='procedimento',
        ),
        migrations.AddField(
            model_name='criarorcamento',
            name='procedimento',
            field=models.ManyToManyField(to='OrcamentoPaciente.procedimento'),
        ),
    ]
