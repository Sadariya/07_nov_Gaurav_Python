# Generated by Django 4.1.5 on 2023-02-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_product_mst_table_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_mst_table',
            name='Product_image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
