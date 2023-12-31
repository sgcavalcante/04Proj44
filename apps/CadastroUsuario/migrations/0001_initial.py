# Generated by Django 4.2.6 on 2023-10-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroPacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=40)),
                ('profissao', models.CharField(max_length=40)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('cidade', models.CharField(blank=True, max_length=20, null=True)),
                ('bairro', models.CharField(blank=True, max_length=20, null=True)),
                ('rua', models.CharField(blank=True, max_length=20, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('complemento', models.TextField(blank=True, max_length=400, null=True)),
                ('alergia', models.CharField(max_length=400)),
                ('doencas_conhecidas', models.CharField(max_length=400)),
            ],
        ),
    ]
