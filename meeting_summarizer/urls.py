# my_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordingUploadView, RecordingViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'recordings', RecordingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', RecordingUploadView.as_view(), name='recording-upload')
]