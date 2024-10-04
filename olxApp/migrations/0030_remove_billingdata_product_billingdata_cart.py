# Generated by Django 4.2.6 on 2023-11-16 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0029_billingdata_buyer_billingdata_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingdata',
            name='product',
        ),
        migrations.AddField(
            model_name='billingdata',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='olxApp.cartmodel'),
        ),
    ]
