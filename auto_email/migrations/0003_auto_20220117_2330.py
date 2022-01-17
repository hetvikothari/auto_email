# Generated by Django 3.2.11 on 2022-01-17 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_email', '0002_auto_20220117_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Chennai', 'Chennai'), ('Banglore', 'Banglore'), ('Kolkata', 'Kolkata')], help_text="Enter reciever's city", max_length=20),
        ),
        migrations.AlterField(
            model_name='mail',
            name='time',
            field=models.TimeField(blank=True, default='23:30:57', null=True),
        ),
    ]