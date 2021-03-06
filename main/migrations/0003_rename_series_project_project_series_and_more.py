# Generated by Django 4.0.2 on 2022-03-10 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_project_project_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='series',
            new_name='project_series',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='slug',
            new_name='project_slug',
        ),
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 0, 6, 5, 416589), verbose_name='date published'),
        ),
    ]
