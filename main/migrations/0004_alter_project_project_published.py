# Generated by Django 4.0.2 on 2022-03-10 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_series_project_project_series_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 0, 57, 22, 609276), verbose_name='date published'),
        ),
    ]