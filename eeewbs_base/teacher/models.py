from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=64)
    sex = models.SmallIntegerField(default=-1)
    title = models.CharField(max_length=512)
    avatar = models.ImageField()
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return "{}  {}".format(self.name, self.title)


class Project(models.Model):
    name = models.CharField(max_length=128)
    industry = models.CharField(max_length=32, null=True)
    start_time = models.DateField()
    team_size = models.IntegerField(default=-1)
    owner = models.BooleanField(default=None)
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return "{}  {}".format(self.name, self.industry)


class Student(models.Model):
    name = models.CharField(max_length=64)
    sex = models.SmallIntegerField(default=-1, verbose_name='性别', choices=((-1, '保密'), (1, '女'), (0, '男')))
    phone_regex = RegexValidator(regex=r'^(1?\d{10})$',
                                 message="手机号码格式为: '1xxxxxxxxxx'. Up to 11 digits allowed.",
                                 code="error phone style")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)  # validators should be a list
    age_regex = RegexValidator(regex=r'^(1[8-9]|[2-9]\d)$',
                               message="年龄为18-99的数字",
                               code='error age')
    age = models.SmallIntegerField(default=20, validators=[age_regex], verbose_name='年龄(18-99)')
    region = models.CharField(max_length=128, null=True, blank=True)
    date_joined = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{}  {}".format(self.name, self.project)


class Course(models.Model):
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField(default=-1)
    time = models.DateField()
    background = models.ImageField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return "{}  {}".format(self.name, self.time)


class Specialization(models.Model):
    name = models.CharField(max_length=64)
    type = models.SmallIntegerField(default=-1)
    desc = models.CharField(max_length=512)
    background = models.ImageField()
    date_joined = models.DateField(auto_now=True)

    def __str__(self):
        return "{}  {}".format(self.name, self.desc)