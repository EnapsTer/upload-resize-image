# Generated by Django 2.1.5 on 2019-06-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_imageurl'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageURL',
        ),
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images', width_field='width_field'),
        ),
    ]
