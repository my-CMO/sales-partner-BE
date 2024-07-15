# my_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingViewSet, RecordingViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'meetings', MeetingViewSet)
router.register(r'recordings', RecordingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]