# Generated by Django 2.2.4 on 2019-08-13 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenue_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='witdrawal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='witdrawal_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
