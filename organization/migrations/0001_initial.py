# Generated by Django 3.0.5 on 2021-05-11 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestBloodDonationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('startDate', models.CharField(max_length=100)),
                ('endDate', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('request_by_hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
            ],
        ),
    ]