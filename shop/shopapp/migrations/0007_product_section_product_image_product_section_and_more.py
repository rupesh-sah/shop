# Generated by Django 4.0.3 on 2022-03-14 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_category_main_category_sub_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField()),
                ('Availability', models.IntegerField()),
                ('featured_image', models.CharField(max_length=500)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Product_Information', models.TextField()),
                ('model_Name', models.CharField(max_length=100)),
                ('Tags', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_url', models.CharField(max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shopapp.section'),
        ),
        migrations.CreateModel(
            name='Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.product')),
            ],
        ),
    ]