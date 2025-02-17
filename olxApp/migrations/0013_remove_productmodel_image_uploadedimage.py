# Generated by Django 4.2.3 on 2023-09-27 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0012_remove_productmodel_product_img_productmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='olxApp.productmodel')),
            ],
        ),
    ]
