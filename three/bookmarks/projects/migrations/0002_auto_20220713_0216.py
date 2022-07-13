# Generated by Django 3.0.14 on 2022-07-12 20:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_time_logout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='login_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]