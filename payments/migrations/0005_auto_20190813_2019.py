# Generated by Django 2.2.4 on 2019-08-13 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20190813_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revenue',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='witdrawal',
            name='approved',
        ),
    ]