# Generated by Django 4.0.2 on 2022-03-10 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_project_project_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 0, 58, 24, 490848), verbose_name='date published'),
        ),
    ]
