# Generated by Django 5.0.2 on 2024-04-08 06:12

import jobsPy.jobs.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(validators=[jobsPy.jobs.validators.validate_deadline_after_today]),
        ),
    ]
