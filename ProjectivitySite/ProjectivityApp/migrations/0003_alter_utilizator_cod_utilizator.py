# Generated by Django 4.2.2 on 2023-06-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectivityApp', '0002_alter_utilizator_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizator',
            name='cod_utilizator',
            field=models.TextField(max_length=50, null=True, unique=True),
        ),
    ]
