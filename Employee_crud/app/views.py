from django.db.models import Model
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from app.models import Employee
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

               # using drf
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import mixins,generics
#---------------------------------------------------------------------------------------------------------------#
#USING VIEW

#reading all records
# class Employeelist(View):
#     def get(self,request):
#         s=Employee.objects.all()
#         data=list(s.values())
#         return JsonResponse(data,safe=False)


#USING APIVIEW CLASS

# class EmployeeList(APIView):
#     def get(self,request):
#         #reads all records from db table
#         s=Employee.objects.all()
#
#         # calls employeeserializer class for converting qs into python native type
#         serializer_instance=EmployeeSerializer(s,many=True)   #when multiple records exists we use many True
#
#         #send the serialized data into client side as json using Response()
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)

#USING MIXIN CLASS

# class EmployeeList(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
#     def get(self,request):
#         return self.list(request)

#USING GENERICS

# class EmployeeList(generics.ListAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#---------------------------------------------------------------------------------------------------------------#


#USING VIEW
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

#USING APIVIEW
# class EmployeeCreate(APIView):
#     def post(self,request):
#
#         data=request.data       #python native type
#
#         #calls EmployeeSerializer for deserialization
#         serializer_instance=EmployeeSerializer(data=request.data)    # or we can write data=data
#
#         #checks whether request.data is valid. if valid the validated data saved to table
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response({'message':'created'},status=status.HTTP_201_CREATED)
#         #if not valid it will raise errors
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#USING MIXINS CLASS
# class EmployeeCreate(mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def post(self, request):
#         return self.create(request)


#USING GENERICS

# class EmployeeCreate(generics.CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#---------------------------------------------------------------------------------------------------------------#


#USING VIEW
#read a specific record(retrieve)
# class EmployeeDetail(View):
#     def get(self,request,i):
#         qs=Employee.objects.filter(id=i)
#         data=list(qs.values())
#         return JsonResponse(data,safe=False)


#USING APIVIEW
# from django.shortcuts import get_object_or_404
# class EmployeeRetrieve(APIView):
#     def get(self, request,i):  #i--parameters receives the id value coming from client side
#
#
#         #Reads the data db table Employee
#         # e=Employee.objects.get(id=i)  #e--model object(django format)
#
#         e=get_object_or_404(Employee,id=i)
#
#
#         #converts the model object(django format) into python native type using EmployeeSerializer
#         serializer_instance=EmployeeSerializer(e)
#
#         #sends the response back to client
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)

#USING MIXIN CLASS

# class EmployeeRetrieve(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get(self, request,pk):
#         return self.retrieve(request,pk)
#

#USING GENERICS
# class EmployeeRetrieve(generics.RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#---------------------------------------------------------------------------------------------------------------#


#USING VIEW
# #update a record fully
# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeeUpdate(View):
#     def put(self,request,i):
#         e=Employee.objects.get(id=i)
#         form_data=request.body
#         data=loads(form_data)
#         e.empid=data['empid']
#         e.name=data['name']
#         e.age=data['age']
#         e.gender=data['gender']
#         e.salary=data['salary']
#         e.designation=data['designation']
#         e.joining_date=data['joining_date']
#
#         e.save()
#         return JsonResponse({'message':'updated'})

#USING APIVIEW
# class EmployeeUpdate(APIView):
#     def put(self,request,i):
#
#
#         #fetches the data coming from client side
#
#         data=request.data
#
#        #Reads the record coming from db table matching with id
#         e=get_object_or_404(Employee,id=i)
#
#        #calls the serializer class for deserialization(conversion+validation)
#         serializer_instance = EmployeeSerializer(instance=e,data=data)
#
#        #After validation saves the record
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#
#        #Returns response back to the client
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#
#        #if is_valid() returns false
#
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#USING MIXIN CLASS
# class EmployeeUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def put(self, request,pk):
#         return self.update(request,pk)

#USING GENERICS
# class EmployeeUpdate(generics.UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer


#---------------------------------------------------------------------------------------------------------------#

#USING VIEW
# #partilaly update
# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeePartialUpdate(View):
#     def patch(self,request,i):
#         e=Employee.objects.get(id=i)
#         form_data=request.body
#
#         data=loads(form_data)
#         print(data)
#
#         if 'empid' in data:
#             e.empid=data['empid']
#
#         if 'name' in data:
#             e.name=data['name']
#
#         if 'age' in data:
#             e.age=data['age']
#
#         if 'gender' in data:
#             e.gender=data['gender']
#
#         if 'salary' in data:
#             e.salary=data['salary']
#
#         if 'designation' in data:
#             e.designation=data['designation']
#
#         if 'joining_date' in data:
#             e.joining_date=data['joining_date']
#
#         e.save()
#         return JsonResponse({'message':'updated'})

#USING APIVIEW
# class EmployeePartialUpdate(APIView):
#     def patch(self, request, i):
#
#         # fetches the data coming from client side
#
#         data = request.data
#
#         # Reads the record coming from db table matching with id
#         e = get_object_or_404(Employee,id=i)
#
#         # calls the serializer class for deserialization(conversion+validation)
#         serializer_instance = EmployeeSerializer(instance=e, data=data,partial=True)
#
#         # After validation saves the record
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#
#             # Returns response back to the client
#
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#
#         # if is_valid() returns false
#
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#USING MIXIN CLASS
# class EmployeePartialUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def patch(self, request,pk):
#         return self.partial_update(request,pk)

#USING GENERICS
# class EmployeePartialUpdate(generics.UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer


#---------------------------------------------------------------------------------------------------------------#

#USING VIEW
# #to delete
# @method_decorator(csrf_exempt,name="dispatch")
# class EmployeeDelete(View):
#     def delete(self,request,i):
#         #reads the record matching with the id from db table
#          s=Employee.objects.get(id=i)
#
#         # delete the record
#          s.delete()
#
#         #send the response
#          return JsonResponse({"message":"deleted successfully"})


#USING APIVIEW
# class EmployeeDelete(APIView):
#      def delete(self,request,i):
#
#
#          #reads the employee record from db table
#          e=get_object_or_404(Employee,id=i)
#
#          #deletes the record
#          e.delete()
#
#          #sends response back to client
#
#          return Response({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)


#USING MIXIN CLASS
# class EmployeeDelete(mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def delete(self, request,pk):
#         return self.destroy(request,pk)

#USING GENERICS
# class EmployeeDelete(generics.DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer



###############################################################################################################

from rest_framework import viewsets
class EmployeeView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer