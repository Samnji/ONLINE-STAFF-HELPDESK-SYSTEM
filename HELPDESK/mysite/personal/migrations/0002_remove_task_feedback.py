# Generated by Django 3.2.4 on 2021-08-17 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='feedback',
        ),
    ]