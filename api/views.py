from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action #method kodukknm,

from api.models import Employees
from api.serializers import EmployeeSerializer




class EmployeeModelViewSetView(viewsets.ModelViewSet):
    serializer_class=EmployeeSerializer
    model=Employees
    queryset=Employees.objects.all()

 #http://127.0.0.1:8000/api/v2/employees/
    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)

        

#method   method=put or get or post or delete

#for filter by departments this custom 

    @action(methods=["get"],detail=False) #detail means passing ids here it is false no id passing
    def departments(self,request,*args,**kwargs):
        data=Employees.objects.all().values_list("department",flat=True)
        return Response(data=data)