# Generated by Django 4.1.3 on 2022-12-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0008_alter_local_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='imagem',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
