# Generated by Django 5.1.3 on 2024-11-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
