# Generated by Django 2.1.7 on 2019-04-01 14:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190401_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 1, 14, 18, 2, 969634, tzinfo=utc)),
        ),
    ]
