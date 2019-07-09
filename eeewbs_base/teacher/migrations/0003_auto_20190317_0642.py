# Generated by Django 2.1.7 on 2019-03-17 06:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('industry', models.CharField(max_length=32)),
                ('start_time', models.DateField()),
                ('team_size', models.IntegerField(default=-1)),
                ('owner', models.BooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sex', models.SmallIntegerField(default=-1)),
                ('phone_number', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="手机号码格式为: '1xxxxxxxxxx'. Up to 11 digits allowed.", regex='^\\1?\\d{9,15}$')])),
                ('age', models.SmallIntegerField(default=-1)),
                ('region', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_joined',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='project',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Student'),
        ),
    ]
