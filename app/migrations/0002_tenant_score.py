# Generated by Django 2.2.10 on 2021-04-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
