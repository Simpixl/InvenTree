# Generated by Django 2.2 on 2019-04-17 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20190417_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='stocktake_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stocktake_stock', to=settings.AUTH_USER_MODEL),
        ),
    ]