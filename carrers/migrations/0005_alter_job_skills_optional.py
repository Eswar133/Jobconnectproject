# Generated by Django 4.2.3 on 2023-08-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrers', '0004_remove_job_duration_of_employment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='skills_optional',
            field=models.ManyToManyField(blank=True, related_name='optional_skills_jobs', to='carrers.skill'),
        ),
    ]