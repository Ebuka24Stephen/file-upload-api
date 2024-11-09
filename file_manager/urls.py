from file_manager.views import FileViewSet  # Import the viewset from the views.py file
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'router', FileViewSet, basename='router')

urlpatterns = [
    path('', include(router.urls)),
]
