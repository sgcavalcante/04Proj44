# Generated by Django 4.2.6 on 2023-12-30 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrcamentoPaciente', '0030_criarorcamento_numero_orcamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamentoitem',
            name='numero_orcamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='OrcamentoPaciente.tb_orcamento'),
        ),
    ]