# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserViewSet, TaskViewSet, TaskCategoryViewSet, 
    TaskUpdateViewSet, EducationalResourceViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'categories', TaskCategoryViewSet)
router.register(r'task-updates', TaskUpdateViewSet, basename='taskupdate')
router.register(r'resources', EducationalResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', UserViewSet.as_view({'post': 'register'}), name='register'),
]