# Generated by Django 4.2.6 on 2023-11-26 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0048_remove_paymentdata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reviewdata',
            name='user',
        ),
    ]
