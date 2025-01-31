# Generated by Django 5.1.5 on 2025-01-29 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('detail', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('subscribe', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('profile_pic', models.ImageField(upload_to='image/')),
                ('resume', models.FileField(upload_to='file/')),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
