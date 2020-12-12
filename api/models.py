from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from authentication.models import User

class Discipline(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, related_name='discipline_owner_fk')
    name = models.CharField(blank=False, null=False, max_length=300)

    def __str__(self):
        return "%s" % self.name

"""    def save(self, *args, **kwargs):
        user = User.get
        super(Discipline, self).save(*args, **kwargs)"""


class Group(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='group_owner_fk', on_delete=models.CASCADE, editable=False)
    name = models.CharField(blank=False, null=False, max_length=150)
    discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='discipline_group_fk')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_list')
    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        self.owner = self.discipline.owner
        super(Group, self).save(*args, **kwargs)


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


class TaskGroup(models.Model):
    task = models.ForeignKey(Task, blank=False, null=False, on_delete=models.CASCADE, related_name='task_group_fk')
    group = models.ForeignKey(Group, blank=False, null=False, on_delete=models.CASCADE, related_name='group_task_fk')

# class StudentDiscipline(models.Model):
#     discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='discipline_fk')
#     user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user_fk')

class Organization(models.Model):
    name  = models.CharField(_('organization_name'), max_length=100)
    code  = models.CharField(_('privilege_code'), max_length=25)
    limit = models.IntegerField(_('limit'))
    def __str__(self):
        return "%s" % self.id
