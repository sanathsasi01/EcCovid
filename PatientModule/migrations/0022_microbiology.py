# Generated by Django 3.2.2 on 2021-05-09 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PatientModule', '0021_rename_other_differentialdiagnosis_others'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microbiology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rt_pcr_covid_date', models.DateField(null=True)),
                ('rt_pcr_covid_result', models.CharField(max_length=20, null=True)),
                ('rapid_anti_body_date', models.CharField(max_length=20, null=True)),
                ('rt_pcr_H1N_date', models.DateField(null=True)),
                ('rt_pcr_H1N_result', models.CharField(max_length=20, null=True)),
                ('viral_culture_date', models.DateField(null=True)),
                ('viral_culture_result', models.CharField(max_length=20, null=True)),
                ('viral_culture_date2', models.DateField(null=True)),
                ('viral_culture_result2', models.CharField(max_length=20, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PatientModule.patientdetails')),
            ],
        ),
    ]
