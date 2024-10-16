# Generated by Django 4.2.6 on 2024-10-15 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CadastroUsuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario', models.DateTimeField()),
                ('descricao', models.CharField(max_length=255)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CadastroUsuario.cadastropacientes')),
            ],
        ),
    ]
