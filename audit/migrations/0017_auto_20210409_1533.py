# Generated by Django 2.2.10 on 2021-04-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0016_checklistinstance_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistinstance',
            name='date_due',
            field=models.DateField(blank=True, null=True),
        ),
    ]
