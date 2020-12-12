from rest_framework import viewsets
from .serizalizers import *
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response


class ContentBlockViewSet(viewsets.ModelViewSet):

    serializer_class = ContentBlockSerializer
    queryset = ContentBlock.objects.all()


class TaskContentBlockListViewSet(viewsets.ModelViewSet):

    serializer_class = TaskContentBlockListSerializer
    queryset = TaskContentBlockList.objects.all()


class ReportContentBlockListViewSet(viewsets.ModelViewSet):

    serializer_class = ReportContentBlockListSerializer
    queryset = ReportContentBlockList.objects.all()


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ReportViewSet(viewsets.ModelViewSet):

    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class TaskCommentViewSet(viewsets.ModelViewSet):

    serializer_class = TaskCommentSerializer
    queryset = TaskComment.objects.all()


class ReportCommentViewSet(viewsets.ModelViewSet):

    serializer_class = ReportCommentSerializer
    queryset = ReportComment.objects.all()


class GroupViewSet(viewsets.ModelViewSet):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class DisciplineViewSet(viewsets.ModelViewSet):

    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()


class GroupStudentViewSet(viewsets.ModelViewSet):
    serializer_class = GroupStudentSerializer
    queryset = Group.objects.all()


class StudentGroupViewSet(viewsets.ModelViewSet):

    serializer_class = StudentGroupSerializer
    queryset = User.objects.all()


class StudentDisciplineViewSet(viewsets.ModelViewSet):

    serializer_class = StudentDisciplineSerializer
    queryset = User.objects.all()


class DisciplineStudentViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplineStudentSerializer
    queryset = Discipline.objects.all() 
