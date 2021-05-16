# Generated by Django 3.0.5 on 2021-05-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('blood', '0007_bloodrequestbyhospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequestbyhospital',
            name='request_by_hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital'),
        ),
    ]