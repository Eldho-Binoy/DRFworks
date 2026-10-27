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

class EmployeeList(APIView):
    def get(self,request):
        #reads all records from db table
        s=Employee.objects.all()

        # calls employeeserializer class for converting qs into python native type
        serializer_instance=EmployeeSerializer(s,many=True)   #when multiple records exists we use many True

        #send the serialized data into client side as json using Response()
        return Response(serializer_instance.data)

#creating aa new employee record
# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeeCreate(View):
#     def post(self,request):
#         form_data=request.body
#
#         data=loads(form_data)
#         print(data)
#         # e=data['empid']
#         # n=data['name']
#         # a=data['age']
#         # g=data['gender']
#         # s=data['salary']
#         # d=data['designation']
#         # j=data['joining_date']
#
#         #e=Employee.objects.create(empid=e,name=n,age=a,gender=g,salary=s,designation=d,joining_date=j)
#         e=Employee.objects.create(**data)
#         e.save()
#
#         return JsonResponse({'message':'created'})
         #using drf
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

#read a specific record
class EmployeeDetail(View):
    def get(self,request,i):
        qs=Employee.objects.filter(id=i)
        data=list(qs.values())
        return JsonResponse(data,safe=False)

#update a record fully
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeUpdate(View):
    def put(self,request,i):
        e=Employee.objects.get(id=i)
        form_data=request.body
        data=loads(form_data)
        e.empid=data['empid']
        e.name=data['name']
        e.age=data['age']
        e.gender=data['gender']
        e.salary=data['salary']
        e.designation=data['designation']
        e.joining_date=data['joining_date']

        e.save()
        return JsonResponse({'message':'updated'})

#partilaly update
@method_decorator(csrf_exempt,name="dispatch")
class EmployeePartialUpdate(View):
    def patch(self,request,i):
        e=Employee.objects.get(id=i)
        form_data=request.body

        data=loads(form_data)
        print(data)

        if 'empid' in data:
            e.empid=data['empid']

        if 'name' in data:
            e.name=data['name']

        if 'age' in data:
            e.age=data['age']

        if 'gender' in data:
            e.gender=data['gender']

        if 'salary' in data:
            e.salary=data['salary']

        if 'designation' in data:
            e.designation=data['designation']

        if 'joining_date' in data:
            e.joining_date=data['joining_date']

        e.save()
        return JsonResponse({'message':'updated'})

#to delete
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeDelete(View):
    def delete(self,request,i):
        #reads the record mathcing with the id from db tble
         s=Employee.objects.get(id=i)

        # delete the record
         s.delete()

        #send the response
         return JsonResponse({"message":"deleted successfully"})