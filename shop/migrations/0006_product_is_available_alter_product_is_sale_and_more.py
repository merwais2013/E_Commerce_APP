# Generated by Django 5.1.3 on 2024-11-17 04:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_star_alter_product_is_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
