# Generated by Django 5.0.2 on 2024-03-09 20:52

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
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(blank=True, null=True, upload_to='company/image')),
                ('website_url', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
