# Generated by Django 2.1.7 on 2019-03-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sex', models.SmallIntegerField()),
                ('title', models.CharField(max_length=512)),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
    ]
