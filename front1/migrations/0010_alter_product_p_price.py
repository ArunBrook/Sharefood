# Generated by Django 4.2.1 on 2023-09-15 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front1', '0009_product_p_localarea_product_p_shopname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='P_price',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
