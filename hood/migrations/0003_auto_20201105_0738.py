# Generated by Django 3.1.2 on 2020-11-05 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20201105_0731'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Authorities',
        ),
        migrations.DeleteModel(
            name='neighbourhood',
        ),
    ]
