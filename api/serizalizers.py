from .models import *
from rest_framework import serializers
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Group
        fields = ('name', 'owner')


class DisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discipline
        fields = '__all__'


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


class ContentBlockListSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='content.type')
    content_content = serializers.CharField(source='content.content')
    comment_fk = CommentSerializer(many=True)

    class Meta:
        model = ContentBlockList
        fields = ('id', 'content_type', 'content_content', 'comment_fk')


class TaskSerializer(serializers.ModelSerializer):
    task_fk = ContentBlockListSerializer(many=True)
    discipline_fk = DisciplineSerializer()
    group_fk = GroupSerializer()

    class Meta:
        model = Task
        fields = ('id', 'discipline_fk', 'group_fk', 'task_fk')
