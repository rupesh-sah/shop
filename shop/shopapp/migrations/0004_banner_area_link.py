# Generated by Django 4.0.3 on 2022-03-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_rename_quote_banner_area_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner_area',
            name='Link',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
