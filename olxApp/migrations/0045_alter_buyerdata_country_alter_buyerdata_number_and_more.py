# Generated by Django 4.2.6 on 2023-11-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0044_buyerdata_address_sellerdata_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerdata',
            name='country',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='buyerdata',
            name='number',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='buyerdata',
            name='state',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='sellerdata',
            name='number',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='sellerdata',
            name='state',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
