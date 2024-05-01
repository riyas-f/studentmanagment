# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [

# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import StudentViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
