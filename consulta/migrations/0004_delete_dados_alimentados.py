# Generated by Django 5.0.1 on 2024-01-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_dados_alimentados_publicado_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dados_alimentados',
        ),
    ]