# Generated by Django 5.0.2 on 2024-03-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('description', models.TextField()),
                ('image_url_1', models.URLField()),
                ('image_url_2', models.URLField(blank=True, null=True)),
            ],
        ),
    ]