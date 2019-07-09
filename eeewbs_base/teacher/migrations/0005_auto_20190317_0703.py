# Generated by Django 2.1.7 on 2019-03-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190317_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='industry',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
    ]
