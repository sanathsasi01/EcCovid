# Generated by Django 3.2.2 on 2021-05-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientModule', '0017_examination'),
    ]

    operations = [
        migrations.CreateModel(
            name='DifferentialDiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('covid19Pneumonitis', models.BooleanField(default=False)),
                ('viralPneumonitis', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='examination',
            name='clubbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='examination',
            name='cyanosis',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='examination',
            name='edema',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='examination',
            name='ictcrus',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='examination',
            name='lymphadenpathy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='examination',
            name='pallor',
            field=models.BooleanField(default=False),
        ),
    ]
