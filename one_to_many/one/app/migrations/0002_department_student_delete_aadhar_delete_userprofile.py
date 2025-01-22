# Generated by Django 5.1.5 on 2025-01-21 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('dep_des', models.TextField(max_length=50)),
                ('dep_hod', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=40)),
                ('std_email', models.EmailField(max_length=254)),
                ('std_roll', models.IntegerField()),
                ('std_dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.department')),
            ],
        ),
        migrations.DeleteModel(
            name='Aadhar',
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]