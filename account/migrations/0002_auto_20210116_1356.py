# Generated by Django 3.1.5 on 2021-01-16 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['id'], 'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
    ]