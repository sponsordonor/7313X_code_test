# Generated by Django 2.0.1 on 2018-02-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givecampus', '0007_auto_20180220_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='state',
            field=models.CharField(choices=[('Active', 'active'), ('Completed', 'completed'), ('Inactive', 'inactive')], default='Active', max_length=20),
        ),
    ]
