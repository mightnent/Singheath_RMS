# Generated by Django 2.2.10 on 2021-03-25 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0007_auto_20210325_1029'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]