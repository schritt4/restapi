# Generated by Django 4.0.4 on 2022-08-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_purpose1_rename_p_image_place_image_place_pur2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='place'),
        ),
    ]