# Generated by Django 2.1.7 on 2019-03-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
    ]
