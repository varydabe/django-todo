# Generated by Django 3.1.1 on 2020-09-30 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user_id',
            new_name='user',
        ),
    ]
