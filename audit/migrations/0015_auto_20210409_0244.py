# Generated by Django 2.2.10 on 2021-04-08 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0014_auto_20210408_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistinstance',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 9)),
        ),
    ]