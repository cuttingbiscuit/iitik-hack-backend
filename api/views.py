from rest_framework import viewsets
from .serizalizers import *



class ContentBlockViewSet(viewsets.ModelViewSet):

    serializer_class = ContentBlockSerializer
    queryset = ContentBlock.objects.all()

    def create(self, request):
        print('QQQQQQQQQQQQQ')
        print(request)
        print(request.user)
        return super().create(request)

class ContentBlockListViewSet(viewsets.ModelViewSet):

    serializer_class = ContentBlockListSerializer
    queryset = ContentBlockList.objects.all()


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class GroupViewSet(viewsets.ModelViewSet):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def create(self, request):
        self.user = request.user
        print(request)
        return super().create(request)


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
