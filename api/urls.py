from django.urls import path
from .views import *
from authentication.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='user')
router.register(r'report', ReportViewSet, basename='user')
router.register(r'contents', ContentBlockViewSet, basename='user')
router.register(r'task_content_lists', TaskContentBlockListViewSet, basename='user')
router.register(r'report_content_lists', ReportContentBlockListViewSet, basename='user')
router.register(r'task_comments', TaskCommentViewSet, basename='user')
router.register(r'report_comments', ReportCommentViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='user')
router.register(r'disciplines', DisciplineViewSet, basename='user')
router.register(r'student_groups', StudentGroupViewSet, basename='user')
router.register(r'student_disciplines', StudentDisciplineViewSet, basename='user')
router.register(r'group_students', GroupStudentViewSet, basename='user')
router.register(r'discipline_students', DisciplineStudentViewSet, basename='user')
router.register(r'users', UserViewSet, basename='user')
router.register(r'reports', ReportViewSet, basename='user')

urlpatterns = router.urls
