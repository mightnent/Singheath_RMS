# Generated by Django 2.2.10 on 2021-04-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0010_auto_20210405_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistinstance',
            name='checklist_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
