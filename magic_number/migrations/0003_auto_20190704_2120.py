# Generated by Django 2.2.3 on 2019-07-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic_number', '0002_auto_20190703_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='banner',
            field=models.ImageField(upload_to='banner/'),
        ),
    ]
