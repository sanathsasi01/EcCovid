# Generated by Django 3.2.2 on 2021-05-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientModule', '0039_patientdetails_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
