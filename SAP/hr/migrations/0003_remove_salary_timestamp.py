# Generated by Django 5.0.4 on 2024-04-30 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='timestamp',
        ),
    ]
