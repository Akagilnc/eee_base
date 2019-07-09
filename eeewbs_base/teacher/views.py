from django.shortcuts import render
from django.contrib.auth.models import User, Group
from eeewbs_base.teacher.models import Teacher, Student, Project, Course, Specialization
from rest_framework import viewsets
from eeewbs_base.teacher.serializers import UserSerializer, GroupSerializer, TeacherSerializer, StudentSerializer, \
    ProjectSerializer, CourseSerializer, SpecializationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Teacher.objects.all().order_by('date_joined')
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('date_joined')
    serializer_class = StudentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('date_joined')
    serializer_class = ProjectSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('date_joined')
    serializer_class = CourseSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Specialization.objects.all().order_by('date_joined')
    serializer_class = SpecializationSerializer