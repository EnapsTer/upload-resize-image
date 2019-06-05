# Generated by Django 2.1.5 on 2019-06-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20190604_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
