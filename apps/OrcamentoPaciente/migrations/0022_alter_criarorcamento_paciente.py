# Generated by Django 4.2.6 on 2023-12-22 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroUsuario', '0017_cadastropacientes_usuario'),
        ('OrcamentoPaciente', '0021_remove_criarorcamento_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criarorcamento',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CadastroUsuario.cadastropacientes'),
        ),
    ]
