
from rest_framework import viewsets
from .serializers import StudentSerializer, DepartmentSerializer
from .models import Student, Department
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUser]
