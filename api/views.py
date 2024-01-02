from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets

class MobileViewSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mobile_object=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(data=request.data,instance=mobile_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        return Response(data={"message":"data deleted successfully"})
