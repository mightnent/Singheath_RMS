# Generated by Django 2.2.10 on 2021-04-19 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppealAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date(2021, 4, 19))),
                ('new_date', models.DateField()),
                ('reason', models.CharField(max_length=1000)),
            ],
        ),
    ]
