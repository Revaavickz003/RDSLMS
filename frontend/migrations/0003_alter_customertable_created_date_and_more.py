# Generated by Django 5.0.4 on 2024-07-05 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_customertable_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertable',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='timestamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 7, 5, 14, 51, 34, 780177)),
        ),
    ]
