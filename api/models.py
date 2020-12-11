from django.db import models


class Discipline(models.Model):
    name = models.CharField(blank=False, null=False, max_length=300)

    def __str__(self):
        return "%s" % self.name


class Group(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150)

    def __str__(self):
        return "%s" % self.name


class ContentBlock(models.Model):
    TYPE = (
        ('FILE', 'file'),
        ('IMAGE', 'image'),
        ('TEXT', 'text'),
    )
    type = models.CharField(null=False, max_length=100, choices=TYPE)
    content = models.CharField(blank=False, null=False, max_length=300)

    def __str__(self):
        return "%s" % self.id


class Task(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    discipline = models.ForeignKey(Discipline, blank=False, null=False, on_delete=models.CASCADE, related_name='discipline_fk')
    group = models.ForeignKey(Group, blank=False, null=False, on_delete=models.CASCADE, related_name='group_fk')
    STATUS = (
        ('SENT', 'sent'),
        ('CHECKED', 'checked'),
        ('VERIFIED', 'verified'),
        ('COMPLETED', 'completed'),
    )
    status = models.CharField(null=False, choices=STATUS, default='SENT', max_length=50)

    def __str__(self):
        return "%s" % self.name


class ContentBlockList(models.Model):
    content = models.ForeignKey(ContentBlock, null=False, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, models.CASCADE, null=False, related_name='task_fk')

    def __str__(self):
        return "%s" % self.id


class Comment(models.Model):
    content = models.CharField(max_length=300)
    begin = models.IntegerField()
    end = models.IntegerField()
    content_block = models.ForeignKey(ContentBlockList, related_name='comment_fk', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id

"""
class StudentGroup(models.Model):
    group = models.ForeignKey(Group, null=False, on_delete=models.CASCADE, related_name='group_fk')
    #user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user_fk')


class StudentDiscipline(models.Model):
    discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='discipline_fk')
    #user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user_fk')
"""