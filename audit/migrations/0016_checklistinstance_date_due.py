# Generated by Django 2.2.10 on 2021-04-09 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0015_auto_20210409_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistinstance',
            name='date_due',
            field=models.DateField(blank=True, default=datetime.date(2021, 4, 9)),
            preserve_default=False,
        ),
    ]