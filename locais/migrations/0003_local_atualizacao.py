# Generated by Django 4.1.3 on 2022-12-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0002_local_dias_func_local_fim_func_local_imagem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
