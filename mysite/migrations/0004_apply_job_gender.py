# Generated by Django 3.2.5 on 2021-07-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_apply_job_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_job',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=30),
        ),
    ]
