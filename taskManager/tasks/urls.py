from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,invite_user,register_with_invite
from django.contrib.admin.views.decorators import staff_member_required

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('invite/', staff_member_required(invite_user), name='invite'),
    path('register/', register_with_invite, name='register'),
]
