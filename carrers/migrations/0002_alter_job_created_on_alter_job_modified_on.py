# Generated by Django 4.2.3 on 2023-08-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
