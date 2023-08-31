# Generated by Django 4.2.1 on 2023-08-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0006_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
