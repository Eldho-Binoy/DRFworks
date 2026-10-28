from django.contrib.postgres import serializers
from django.db.models import Model
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from app.models import Employee
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#reading all records
# class Employeelist(View):
#     def get(self,request):
#         s=Employee.objects.all()
#         data=list(s.values())
#         return JsonResponse(data,safe=False)
               # using drf
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import EmployeeSerializer
from rest_framework import status

class EmployeeList(APIView):
    def get(self,request):
        #reads all records from db table
        s=Employee.objects.all()

        # calls employeeserializer class for converting qs into python native type
        serializer_instance=EmployeeSerializer(s,many=True)   #when multiple records exists we use many True

        #send the serialized data into client side as json using Response()
        return Response(serializer_instance.data)


class EmployeeCreate(APIView):
    def post(self,request):

        data=request.data       #python native type

        #calls EmployeeSerializer for deserialization
        serializer_instance=EmployeeSerializer(data=request.data)    # or we can write data=data

        #checks whether request.data is valid. if valid the validated data saved to table
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({'message':'created'})
        #if not valid it will raise errors
        else:
            return Response(serializer_instance.errors)




from django.shortcuts import get_object_or_404
class EmployeeRetrieve(APIView):
    def get(self,request,i): #i parameter recieves the id value cominf from client
        #fetch id
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)
        #convertion
        serializer_instance=EmployeeSerializer(e)
        #returrn response
        return Response(serializer_instance.data)




class EmployeeUpdate(APIView):
    def put(self,request,i):

        #fetches the data coming from clientside
        data=request.data
        #reads the records from db table matching with id
        e=get_object_or_404(Employee,id=i)
        #calls the serializer class for deserialization
        serializer_instance=EmployeeSerializer(isinstance=e,data=data)

        #after validation saves the respomse
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        #if is_valid() return False
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class EmployeePartialUpdate(APIView):
    def patch(self,request,i):

        #fetches the data coming from clientside
        data=request.data
        #reads the records from db table matching with id
        e=get_object_or_404(Employee,id=i)
        #calls the serializer class for deserialization
        serializer_instance=EmployeeSerializer(instance=e,data=data,partial=True)

        #after validation saves the respomse
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        #if is_valid() return False
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
# #to delete
# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeeDelete(View):
#     def delete(self,request,i):
#         #reads the record mathcing with the id from db tble
#          s=Employee.objects.get(id=i)
#
#         # delete the record
#          s.delete()
#
#         #send the response
#          return JsonResponse({"message":"deleted successfully"})

class EmployeeDelete(APIView):
    def delete(self,request,i):

        #reads the employee record from db table
        e=Employee.objects.get(id=i)

        e.delete()

        return Response({"meseage":"deleted"})
