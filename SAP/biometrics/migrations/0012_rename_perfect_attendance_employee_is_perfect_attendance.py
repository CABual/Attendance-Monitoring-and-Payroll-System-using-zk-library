# Generated by Django 5.0.4 on 2024-05-03 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biometrics', '0011_rename_full_attendance_employee_perfect_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='perfect_attendance',
            new_name='is_perfect_attendance',
        ),
    ]