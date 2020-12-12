from rest_framework import viewsets, views
from .serizalizers import *
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    @receiver(post_save, sender=Report)
    def send_signal_to_tutor(self, sender, instance, created, **kwargs):
        if created:
            print('Report was created')
            #Send signal to tutor

    

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


class TaskFileUploadView(viewsets.ModelViewSet):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        serializer = ContentBlockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(status=400)


class ReportFileUploadView(viewsets.ModelViewSet):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        serializer = ContentBlockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(status=400)


"""    def put(self, request, format=None):
        f = request.data['file']
        destination = open('/media/' + f.name, 'wb+')
        for chunk in f.write(chunk):
            destination.write(chunk)
        destination.close()
        content_block = ContentBlock(type='file', content=f)
        content_block.save()
        task = request.data['task']
        task_content = TaskContentBlockList(content=content_block, task=task)
        task_content.save()
        return Response(status=204)"""
