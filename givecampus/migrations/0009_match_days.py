# Generated by Django 2.0.1 on 2018-02-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givecampus', '0008_auto_20180220_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
