# Generated by Django 2.0.1 on 2018-02-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('givecampus', '0003_auto_20180220_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='title',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
