# Generated by Django 4.2.2 on 2023-06-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectivityApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizator',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
