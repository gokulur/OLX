# Generated by Django 4.2.6 on 2023-11-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0033_billingdata_product_paymentdata_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
