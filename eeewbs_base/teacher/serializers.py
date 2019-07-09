from django.contrib.auth.models import User, Group
from eeewbs_base.teacher.models import Teacher, Project, Student, Course, Specialization
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'name', 'sex', 'title', 'avatar', 'date_joined')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'name', 'sex', 'phone_number', 'age', 'date_joined', 'project')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'name', 'industry', 'start_time', 'team_size', 'owner', 'date_joined')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'name', 'type', 'time', 'background', 'teacher', 'date_joined')


class SpecializationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specialization
        fields = ('url', 'name', 'type', 'desc', 'background', 'date_joined')