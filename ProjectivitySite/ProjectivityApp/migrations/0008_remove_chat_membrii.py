# Generated by Django 4.2.2 on 2023-06-26 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectivityApp', '0007_alter_chat_cod_utilizator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='membrii',
        ),
    ]