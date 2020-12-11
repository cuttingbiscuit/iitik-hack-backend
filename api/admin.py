from django.contrib import admin
from .models import *


class ContentBlockListAdmin(admin.TabularInline):
    model = ContentBlockList
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    inlines = [
        ContentBlockListAdmin
    ]


admin.site.register(ContentBlock)
admin.site.register(ContentBlockList)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment)
