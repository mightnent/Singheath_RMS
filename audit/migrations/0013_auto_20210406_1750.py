# Generated by Django 2.2.10 on 2021-04-06 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0012_checklistinstance_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistinstance',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 6)),
        ),
    ]