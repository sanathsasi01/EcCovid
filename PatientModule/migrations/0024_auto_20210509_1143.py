# Generated by Django 3.2.2 on 2021-05-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientModule', '0023_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='nebulisation_budocort',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='treatment',
            name='nebulisation_budocort_qh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='treatment',
            name='nebulisation_duolin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='treatment',
            name='nebulisation_duolin_qh',
            field=models.BooleanField(default=False),
        ),
    ]
