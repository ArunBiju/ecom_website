# Generated by Django 4.1.3 on 2022-12-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detailpage', '0004_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_category', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Primary Category',
                'verbose_name_plural': 'Primary Categories',
            },
        ),
        migrations.CreateModel(
            name='SecondaryCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Secondary_category', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Secondary CategoryModel',
                'verbose_name_plural': 'Secondary CategoryModels',
            },
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='category',
        ),
        migrations.DeleteModel(
            name='CategoryModel',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='primary_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detailpage.primarycategorymodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='secondary_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detailpage.secondarycategorymodel'),
        ),
    ]
