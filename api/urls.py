from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='user')
router.register(r'content', ContentBlockViewSet, basename='user')
router.register(r'content_list', ContentBlockListViewSet, basename='user')

urlpatterns = router.urls
