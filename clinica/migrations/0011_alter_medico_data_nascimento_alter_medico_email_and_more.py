# Generated by Django 5.1 on 2024-11-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0010_alter_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medico',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
