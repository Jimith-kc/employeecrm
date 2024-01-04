from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action #method kodukknm,

from api.models import Employees,Tasks
from api.serializers import EmployeeSerializer,Taskserializer

from rest_framework import authentication,permissions


class EmployeeModelViewSetView(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAdminUser]
    authentication_classes=[authentication.BasicAuthentication]

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

 #-------------------------------------------------       

#method   method=put or get or post or delete

#for filter by departments this custom 

    @action(methods=["get"],detail=False) #detail means passing ids here it is false no id passing
    def departments(self,request,*args,**kwargs):
        data=Employees.objects.all().values_list("department",flat=True)
        return Response(data=data)


#--------------------------------------------------
#assign new task for a employee
#localhost:8000/api/v2/employees/{id}/add_task/
#custom method aayitt kodukkan pokunnu oru particular employee k thenne aan task add akunnath so puthiya taskview create aakkunila
#method=post
#data={name,status, }
    @action(methods=["post"],detail=True) #add_task is a cusyom method ath thunderclient nu manasialavan vendiyaann ith kodukkunnath
    def add_task(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employees.objects.get(id=id)
        serializer=Taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=employee_object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
#----------------------------------------------------------------
#list all tasks assigned
#localhost:8000/api/v2/employees/{id}/tasks/
#method=get
    @action(methods=["get"],detail=True)
    def tasks(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        #employee_object=Employees.objects.get(id=id)     ith upayogichal database korchoode complicated aavum 
        #qs=Tasks.objects.filter(employee=employee_object)

        qs=Tasks.objects.filter(employee__id=id)
        serializer=Taskserializer(qs,many=True)
        return Response(data=serializer.data)
        

#----------------------------------------------------------------
#update tasks assigned
#localhost:8000/api/v2/employees/task/{taskid)/update
#method=put
    @action(methods=["get"],detail=True)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Tasks.objects.filter(employee__id=id)
        serializer=Taskserializer(qs,many=True)
        return Response(data=serializer.data) 
        