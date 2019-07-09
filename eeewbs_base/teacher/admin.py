
# Register your models here.
from django.contrib import admin
from .models import Teacher, Project, Student

admin.site.register(Teacher)
admin.site.register(Project)
admin.site.register(Student)
