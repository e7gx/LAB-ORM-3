# Generated by Django 5.0.7 on 2024-07-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
