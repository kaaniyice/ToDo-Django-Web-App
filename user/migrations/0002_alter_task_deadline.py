# Generated by Django 5.0 on 2023-12-23 18:37

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 12, 24, 21, 37, 12, 580752))], verbose_name='Due Date'),
        ),
    ]
