# Generated by Django 4.1.5 on 2023-02-25 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farming_app', '0002_retailer_model_alter_signup_model_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailer_model',
            name='confirmation',
            field=models.CharField(default='Reject', max_length=15),
        ),
        migrations.AlterField(
            model_name='retailer_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 25, 19, 31, 41, 316418)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 25, 19, 31, 41, 315414)),
        ),
    ]
