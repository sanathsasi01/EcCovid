# Generated by Django 3.2 on 2021-04-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('admin', models.BooleanField(default=False)),
                ('hospital', models.BooleanField(default=False)),
                ('doctor', models.BooleanField(default=False)),
                ('patient', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
