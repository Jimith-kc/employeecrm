
from rest_framework import serializers
from api.models import Employees,Tasks


class EmployeeSerializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employees
        fields="__all__"
        read_only_fields=["id"]  

class Taskserializer(serializers.ModelSerializer):

    Employee=serializers.StringRelatedField()
    class Meta:
        model=Tasks
        fields="__all__"
        read_only_fields=["id","employee","assigned_date"]