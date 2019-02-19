# Generated by Django 2.1.4 on 2018-12-27 20:16

from django.db import migrations
from ..models import Mineral


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        # After the database is created, load from the json file
        migrations.RunPython(Mineral.load_from_json),
    ]
