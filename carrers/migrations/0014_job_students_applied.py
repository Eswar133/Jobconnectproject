# Generated by Django 4.2.3 on 2023-08-22 02:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrers', '0013_alter_job_duration_in_months_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='students_applied',
            field=models.ManyToManyField(blank=True, related_name='applied_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
