# Generated by Django 4.0.6 on 2022-07-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_tags_order_customer_order_products_products_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tags',
            new_name='Tag',
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
