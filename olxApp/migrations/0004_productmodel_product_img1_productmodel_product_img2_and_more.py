# Generated by Django 4.2.3 on 2023-08-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0003_productmodel_category_productmodel_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='Product_Img1',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Product_Img2',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='Product_Img3',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
