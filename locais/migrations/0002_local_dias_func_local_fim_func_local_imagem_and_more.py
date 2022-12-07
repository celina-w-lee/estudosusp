# Generated by Django 4.1.3 on 2022-12-06 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='dias_func',
            field=models.CharField(choices=[('Segunda a sexta', 'Segunda a sexta'), ('Todos os dias', 'Todos os dias'), ('Segunda a sábado', 'Segunda a sábado'), ('Verificar no local', 'Verificar no local')], default='Segunda a sexta', max_length=50),
        ),
        migrations.AddField(
            model_name='local',
            name='fim_func',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local',
            name='imagem',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local',
            name='inicio_func',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
