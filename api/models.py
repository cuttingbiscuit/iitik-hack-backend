from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Discipline(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, related_name='discipline_owner_fk')
    name = models.CharField(blank=False, null=False, max_length=300)

    def __str__(self):
        return "%s" % self.name


class Group(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='group_owner_fk', on_delete=models.CASCADE, editable=False)
    name = models.CharField(blank=False, null=False, max_length=150)
    discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='discipline_group_fk')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_list', null=True)
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, related_name='user_task_fk')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False, related_name='group_task_fk')
    STATUS = (
        ('OPENED', 'opened'),
        ('CLOSED', 'closed'),
    )
    status = models.CharField(null=False, choices=STATUS, default='CLOSED', max_length=50)

    def __str__(self):
        return "%s" % self.name


class Report(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, null=False, blank=False, default=0, related_name='reciever_report_fk')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False, related_name='task_report_fk')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE, related_name='own_reports_fk')
    STATUS = (
        ('SENT', 'sent'),
        ('OK', 'ok'),
        ('NOT_OK', 'ok'),
    )
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        )
    status = models.CharField(null=False, choices=STATUS, default='SENT', max_length=50)
    rating = models.IntegerField(choices=RATING, blank=True)

    def __str__(self):
        return "%s" % self.name


class TaskContentBlockList(models.Model):
    content = models.ForeignKey(ContentBlock, null=False, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, related_name='task_fk')

    def __str__(self):
        return "%s" % self.id


class ReportContentBlockList(models.Model):
    content = models.ForeignKey(ContentBlock, null=False, blank=False, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=False, related_name='report_fk')
    
    def __str__(self):
        return "%s" % self.id


class TaskComment(models.Model):
    content = models.CharField(max_length=300)
    begin = models.IntegerField()
    end = models.IntegerField()
    content_block = models.ForeignKey(TaskContentBlockList, related_name='task_comment_fk', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id


class ReportComment(models.Model):
    content = models.CharField(max_length=300)
    begin = models.IntegerField()
    end = models.IntegerField()
    content_block = models.ForeignKey(ReportContentBlockList, related_name='report_comment_fk', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.id