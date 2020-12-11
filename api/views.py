from rest_framework import viewsets
from .serizalizers import *


class ContentBlockViewSet(viewsets.ModelViewSet):

    serializer_class = ContentBlockSerializer
    queryset = ContentBlock.objects.all()


class ContentBlockListViewSet(viewsets.ModelViewSet):

    serializer_class = ContentBlockListSerializer
    queryset = ContentBlockList.objects.all()


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
