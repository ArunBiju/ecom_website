# Generated by Django 4.1.3 on 2022-12-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailpage', '0002_alter_categorymodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_image_1',
            field=models.ImageField(null=True, upload_to='product_image'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_image_2',
            field=models.ImageField(null=True, upload_to='product_image'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_image_3',
            field=models.ImageField(null=True, upload_to='product_image'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails'),
        ),
    ]
