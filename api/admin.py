from django.contrib import admin
from .models import *


class TaskContentBlockListAdmin(admin.TabularInline):
    model = TaskContentBlockList
    extra = 1


class ReportContentBlockListAdmin(admin.TabularInline):
    model = ReportContentBlockList
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    inlines = [
        TaskContentBlockListAdmin
    ]


class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReportContentBlockListAdmin
    ]


admin.site.register(ContentBlock)
admin.site.register(TaskContentBlockList)
admin.site.register(ReportContentBlockList)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment)
admin.site.register(ReportComment)
admin.site.register(Discipline)
admin.site.register(Group)
admin.site.register(Report, ReportAdmin)
