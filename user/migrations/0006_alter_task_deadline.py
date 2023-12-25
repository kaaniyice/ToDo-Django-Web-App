# Generated by Django 5.0 on 2023-12-23 21:14

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 12, 25, 0, 14, 40, 859820))], verbose_name='Due Date'),
        ),
    ]