# Generated by Django 4.0.1 on 2022-01-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=100),
        ),
    ]
