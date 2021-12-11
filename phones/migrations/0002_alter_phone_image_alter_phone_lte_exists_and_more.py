# Generated by Django 4.0 on 2021-12-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]