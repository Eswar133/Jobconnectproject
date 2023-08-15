from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrers', '0008_alter_job_company_info_alter_job_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_info',
            field=models.ForeignKey(default=1, on_delete=models.deletion.CASCADE, to='carrers.company'),
            
        ),
    ]
