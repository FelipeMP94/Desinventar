# Generated by Django 5.0.1 on 2024-01-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0002_dados_alimentados'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados_alimentados',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registros_desastres',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
