# Generated by Django 5.1 on 2024-11-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0012_consultaagendada_especialidadeclinica_exameagendado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exameclinica',
            name='descricao',
            field=models.TextField(null=True),
        ),
    ]
