# Generated by Django 2.2 on 2019-06-22 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysandwich', '0008_auto_20190620_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='price',
        ),
    ]
