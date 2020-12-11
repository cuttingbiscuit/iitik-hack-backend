from .models import *
from rest_framework import serializers


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

    class Meta:
        model = Task
        fields = ('id', 'discipline_name', 'group_name', 'task_fk')
