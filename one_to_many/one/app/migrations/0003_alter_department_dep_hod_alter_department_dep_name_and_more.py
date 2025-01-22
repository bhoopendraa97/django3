# Generated by Django 5.1.5 on 2025-01-21 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_department_student_delete_aadhar_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_hod',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='std_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.department', to_field='dep_name'),
        ),
    ]
