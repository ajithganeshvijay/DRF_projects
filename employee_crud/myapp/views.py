from django.shortcuts import render

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from django.views import View

from myapp import serializers
from myapp.models import Employee
# Create your views here.

# GET method
#APPIView for reading all employee records
from myapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
class Employeelist(APIView):
    def get(self,request):
        data=Employee.objects.all()#Read all employee records from employee table(data)
        serializer_instance=EmployeeSerializer(data,many=True)
        # EmployeeSerializer coverts queryset into python native types
        #queryset contains more than one records we are using (many=True)
        return Response(serializer_instance.data)#converts python native type to Json fromat

#POST Method
import json
# APIView for create new Employee record
class EmployeeCreateList(APIView):
    def post(self,request):
        # Views receives data as request.data(client side data _python native type)

        #Calls Serializer class for deserialization here we pass request.data as argument

        # after validation serializer saves data as model object inside db table
        serializer_instances=EmployeeSerializer(data=request.data) #Deserialization
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response({"message":"Created successfully"})
        else:
            return Response(serializer_instances.errors,status=400)



#GET method by using specific id:
# APIView for read specific record using ID
from django.shortcuts import get_object_or_404
class EmployeeDetail(APIView):
    def get(self,request,i):
        # data=Employee.objects.get(empid=i)
        data=get_object_or_404(Employee,id=i)
        serializer_instances=EmployeeSerializer(data)
        if serializer_instances:
            return Response(serializer_instances.data)
        else:
            return Response({"Message":"Data not found"})

#PUT request method:
# APIView for Fully update a specific record using ID
class EmployeeDetailUpdate(APIView):
    def put(self,request,i):
        e=Employee.objects.get(id=i)
        serializer_instance=EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)



#patch method:
import json

class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        e=Employee.objects.get(id=i)
        serializer_instance=EmployeeSerializer(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

#DELETE method
import json
class EmployeeDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({"messagae":"Employee details deleted successfully!"})


