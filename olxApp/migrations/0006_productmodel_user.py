# Generated by Django 4.2.3 on 2023-09-15 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olxApp', '0005_buyerdata_alter_cartmodel_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
