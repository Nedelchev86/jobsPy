# Generated by Django 5.0.2 on 2024-03-02 19:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('website', models.CharField(blank=True, max_length=70, null=True)),
                ('linkedin', models.CharField(max_length=50)),
                ('github', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Devorced', 'Devorced')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='jobseekers.jobseeker')),
            ],
        ),
    ]
