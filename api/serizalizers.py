from .models import *
from rest_framework import serializers
from authentication.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    users = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ('name', 'owner', 'users')

    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class DisciplineSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    users = UserSerializer(many=True)

    class Meta:
        model = Discipline
        fields = ('id', 'name', 'owner', 'users')
        
    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class ContentBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentBlock
        fields = '__all__'

    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'begin', 'end')

    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class ContentBlockListSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='content.type')
    content_content = serializers.CharField(source='content.content')
    comment_fk = CommentSerializer(many=True)

    class Meta:
        model = ContentBlockList
        fields = ('id', 'content_type', 'content_content', 'comment_fk')

    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    task_fk = ContentBlockListSerializer(many=True)
    group = GroupSerializer()
    discipline = DisciplineSerializer()

    class Meta:
        model = Task
        fields = ('id', 'discipline', 'group', 'task_fk')

    def create(self, validated_data):
        return ContentBlock.objects.create(**validated_data)


class GroupStudentSerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'users')


class StudentGroupSerializer(serializers.ModelSerializer):

    group_list = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'group_list')


class DisciplineStudentSerializer(serializers.ModelSerializer):
    
    discipline_group_fk = GroupStudentSerializer(many=True)

    class Meta:
        model = Discipline
        fields = ('id', 'discipline_group_fk')


class StudentDisciplineSerializer(serializers.ModelSerializer):
    
    discipline = serializers.CharField(source='discipline.name')

    class Meta:
        model = User
        fields = ('id', 'name', 'discipline')
