# Generated by Django 4.0.3 on 2022-03-11 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_banner_area_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner_area',
            old_name='DISCOUNT_DEAL',
            new_name='Discount_Deal',
        ),
        migrations.RenameField(
            model_name='banner_area',
            old_name='Image',
            new_name='image',
        ),
    ]
