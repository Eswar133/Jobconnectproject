# Generated by Django 4.2.3 on 2023-08-15 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrers', '0009_alter_job_company_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carrers.company'),
        ),
    ]
