# Generated by Django 2.0.1 on 2018-02-20 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('givecampus', '0006_auto_20180220_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='donor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='givecampus.Donor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sponsor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='givecampus.Sponsor'),
        ),
    ]
