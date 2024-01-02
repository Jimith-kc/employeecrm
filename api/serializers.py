
from rest_framework import serializers
from api.models import bEmployees


class EmployeeSerializer(serializers.ModelSerializers):
    
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employees
        fields="__all__"
        read_only_fields=["id"]  