# Generated by Django 4.2.3 on 2023-08-27 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrers', '0015_company_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='skills_mandatory',
            field=models.ManyToManyField(related_name='mandatory_jobs', to='carrers.skill'),
        ),
        migrations.AlterField(
            model_name='job',
            name='skills_optional',
            field=models.ManyToManyField(related_name='optional_jobs', to='carrers.skill'),
        ),
    ]
