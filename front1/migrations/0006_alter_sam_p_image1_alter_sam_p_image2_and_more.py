# Generated by Django 4.2.1 on 2023-09-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front1', '0005_sam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sam',
            name='P_image1',
            field=models.ImageField(blank=True, null=True, upload_to='B_product/'),
        ),
        migrations.AlterField(
            model_name='sam',
            name='P_image2',
            field=models.ImageField(blank=True, null=True, upload_to='B_product/'),
        ),
        migrations.AlterField(
            model_name='sam',
            name='P_image3',
            field=models.ImageField(blank=True, null=True, upload_to='B_product/'),
        ),
    ]
