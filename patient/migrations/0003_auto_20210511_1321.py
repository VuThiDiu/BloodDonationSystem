# Generated by Django 3.0.5 on 2021-05-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20210511_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
