# Generated by Django 3.1.1 on 2020-09-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201001_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]