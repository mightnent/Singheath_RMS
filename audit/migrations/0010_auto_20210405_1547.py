# Generated by Django 2.2.10 on 2021-04-05 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0009_auto_20210405_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistinstance',
            name='tenant',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checklistinstance',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 5)),
        ),
    ]
