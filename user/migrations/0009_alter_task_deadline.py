# Generated by Django 5.0 on 2023-12-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Due Date'),
        ),
    ]
