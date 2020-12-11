from django.db import models

class ContentBlock(models.Model):
    TYPE = (
        ('FILE', 'file'),
        ('IMAGE', 'image'),
        ('TEXT', 'text'),
    )
    type = models.CharField(null=False, max_length=100, choices=TYPE)
    content = models.CharField(blank=False, null=False, max_length=300)

class Task(models.Model):
    discipline_name = models.CharField(blank=False, null=False, max_length=300)
    group_name = models.CharField(blank=False, null=False, max_length=300)


class ContentBlockList(models.Model):
    content = models.ForeignKey(ContentBlock, null=False, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, models.CASCADE, null=False, related_name='task_fk')


class Comment(models.Model):
    content = models.CharField(max_length=300)
    begin = models.IntegerField()
    end = models.IntegerField()
    content_block = models.ForeignKey(ContentBlockList, related_name='comment_fk', on_delete=models.CASCADE)
