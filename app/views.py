from django.shortcuts import render
from app.models import *
from app.serializers import *

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class Productdata(ViewSet):
    def list(self,request):
        PD=Product.objects.all()
        JCD=ProductModelSerializer(PD,many=True)
        return Response(JCD.data)
    def retrieve(self,request,pk):
        PD=Product.objects.get(pid=pk)
        JCD=ProductModelSerializer(PD)
        return Response(JCD.data)
    def create(self,request):
        PO=request.data
        JCD=ProductModelSerializer(data=PO)
        if JCD.is_valid():
            JCD.save()
            return Response({"message":"data is inserted"})
        else:
            return Response({"message":"data is not inserted"})
    def update(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JCD=ProductModelSerializer(PO,data=request.data)
        if JCD.is_valid():
            JCD.save()
            return Response({"message":"data is updated"})
        else:
            return Response({"message":"data is not updated"})
        
    def partial_update(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JCD=ProductModelSerializer(PO,data=request.data,partial=True)
        if JCD.is_valid():
            JCD.save()
            return Response({"message":"data is updated"})
        else:
            return Response({"message":"data is not updated"})
        
    def destroy(self,request,pk):
        PO=Product.objects.get(pid=pk)
        PO.delete()
        return Response({"message":"data is deleted"})

        
            

            
            

