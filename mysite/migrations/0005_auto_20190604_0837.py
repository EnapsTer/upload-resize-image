# Generated by Django 2.1.5 on 2019-06-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190604_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field'),
        ),
    ]
