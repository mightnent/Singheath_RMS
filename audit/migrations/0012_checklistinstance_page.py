# Generated by Django 2.2.10 on 2021-04-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0011_checklistinstance_checklist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistinstance',
            name='page',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
