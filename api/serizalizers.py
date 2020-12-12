from .models import *
from rest_framework import serializers
from authentication.serializers import UserSerializer
from authentication.models import User

class GroupSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    users = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ('name', 'owner', 'users')

    def create(self, validated_data):
        return Group.objects.create(**validated_data)


class DisciplineSerializer(serializers.ModelSerializer):

    owner = UserSerializer()

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'owner')
        
    def create(self, validated_data):
        return Discipline.objects.create(**validated_data)


class ContentBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentBlock
        fields = '__all__'

    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class TaskCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskComment
        fields = ('id', 'content', 'begin', 'end')

    def create(self, validated_data):
        return TaskComment.objects.create(**validated_data)


class ReportCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportComment
        fields = ('id', 'content', 'begin', 'end')

    def create(self, validated_data):
        return ReportComment.objects.create(**validated_data)


class TaskContentBlockListSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='content.type')
    content_content = serializers.CharField(source='content.content')
    comment_fk = TaskCommentSerializer(many=True)
    task_id = serializers.CharField(source='task.id')

    class Meta:
        model = TaskContentBlockList
        fields = ('id', 'content_type', 'content_content', 'comment_fk', 'task_id')

    def create(self, validated_data):
        return TaskContentBlockList.objects.create(**validated_data)


class ReportContentBlockListSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='content.type')
    content_content = serializers.CharField(source='content.content')
    comment_fk = ReportCommentSerializer(many=True)
    report_id = serializers.CharField(source='report.id')

    class Meta:
        model = ReportContentBlockList
        fields = ('id', 'content_type', 'content_content', 'report_comment_fk', 'report_id')

    def create(self, validated_data):
        return ReportContentBlockList.objects.create(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    task_fk = TaskContentBlockListSerializer(many=True)
    group = GroupSerializer()
    owner = UserSerializer()

    class Meta:
        model = Task
        fields = ('id', 'owner', 'group', 'task_fk')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)


class GroupTask(serializers.ModelSerializer):

    task_fk = TaskContentBlockListSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'task_fk')

class ReportSerializer(serializers.ModelSerializer):
    report_fk = ReportContentBlockListSerializer
    reciever = UserSerializer()
    task_id = serializers.IntegerField(source='task.id')
    owner = UserSerializer()

    class Meta:
        model = Report
        fields = ('id', 'name', 'reciever', 'task_id', 'owner', 'status', 'rating')


class GroupStudentSerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True)
    group_task_fk = GroupTask(many=True)

    class Meta:
        model = Group
        fields = ('id', 'users', 'group_task_fk')


class StudentGroupSerializer(serializers.ModelSerializer):

    group_list = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'group_list')


class DisciplineStudentSerializer(serializers.ModelSerializer):
    
    owner = UserSerializer()
    discipline_group_fk = GroupStudentSerializer(many=True)

    class Meta:
        model = Discipline
        fields = ('id', 'owner', 'discipline_group_fk')


                #Чинить ↓↓↓↓↓
class StudentDisciplineSerializer(serializers.ModelSerializer):
    
    discipline = serializers.CharField(source='discipline.name')

    class Meta:
        model = User
        fields = ('id', 'name', 'discipline')



