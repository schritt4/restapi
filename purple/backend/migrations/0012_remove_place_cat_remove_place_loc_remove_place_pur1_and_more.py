# Generated by Django 4.0.4 on 2022-08-12 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_place_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='place',
            name='loc',
        ),
        migrations.RemoveField(
            model_name='place',
            name='pur1',
        ),
        migrations.RemoveField(
            model_name='place',
            name='pur2',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Purpose1',
        ),
        migrations.DeleteModel(
            name='Purpose2',
        ),
    ]
