# Generated by Django 2.2.16 on 2022-04-06 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': ('Пользователь',), 'verbose_name_plural': 'Пользователи'},
        ),
    ]