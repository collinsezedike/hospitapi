from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from api.models import Department, Staff
from api.serializers import DepartmentSerializer, StaffSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("-created_on")
    serializer_class = DepartmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by("-first_name")
    serializer_class = StaffSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
