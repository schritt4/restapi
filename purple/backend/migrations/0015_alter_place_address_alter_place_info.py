# Generated by Django 4.0.4 on 2022-08-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_merge_20220813_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
