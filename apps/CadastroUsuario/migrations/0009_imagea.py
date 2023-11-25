# Generated by Django 4.2.6 on 2023-11-20 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroUsuario', '0008_alter_cadastropacientes_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('imagem', models.ImageField(default=None, upload_to='images/')),
                ('nome', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CadastroUsuario.cadastropacientes')),
            ],
        ),
    ]
