# Generated by Django 2.0.1 on 2018-02-20 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('givecampus', '0004_auto_20180220_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
