# Generated by Django 3.0.5 on 2021-05-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_bloodrequest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='hospitalID',
            field=models.CharField(default='hospitalID', max_length=30),
        ),
    ]