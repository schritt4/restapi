# Generated by Django 4.1 on 2022-08-05 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curation',
            old_name='author',
            new_name='user',
        ),
    ]
