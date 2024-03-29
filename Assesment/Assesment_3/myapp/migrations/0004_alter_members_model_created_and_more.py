# Generated by Django 4.1.5 on 2023-03-04 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_signup_model_mail_alter_members_model_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 4, 14, 31, 14, 607627)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 4, 14, 31, 14, 607627)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
