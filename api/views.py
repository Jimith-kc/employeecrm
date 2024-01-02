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

#url mention  lh:8000/api/v2/employees/departments/
#method   method=put or get or post or delete

#for filter by departments this custom 

    @action(methods=["get"],detail=False) #detail means passing ids here it is false no id passing
    def departments(self,request,*args,**kwargs):
        data=Employees.objects.all().values_list("department",flat=True)
        return Response(data=data)



#class EmployeeModelViewSetView(viewsets.ViewSet):

    
    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data={"message":"data deleted successfully"})
