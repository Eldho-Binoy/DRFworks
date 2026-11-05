from django.shortcuts import render,get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from starlette.status import HTTP_201_CREATED

from app import serializers
from app.serializers import DoctorSerializer,UserSerializer

from rest_framework import status
from rest_framework.response import Response



#API VIEW FOR
    #CREATING A NEW DOCTOR RECORD
    #LISTING ALL DOCTORS
    #READING A SPECIFIC DOCTOR
    #UPDATING DETAILS OF A DOCTOR
    #DELETING A DOCTOR RECORD
    #FILTERING DOCTOR DETAILS BASED ON SPECIALIZATION


from rest_framework import status
from app.serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Doctor

class DoctorListCreate(APIView):

    permission_classes=[IsAdminUser]
    authentication_class=[BasicAuthentication]

#CREATING A NEW DOCTOR RECORD
    def post(self,request):
        serializer_instance=DoctorSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#LISTING ALL DOCTORS
    def get(self,request):
        d=Doctor.objects.all()
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class DoctorRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        serializer_instance=DoctorSerializer(d)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        serializer_instance=DoctorSerializer(d,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        pass

class Doctor_filter_serialization(APIView):
    def get(self,request):
        data=request.query_params.get('search')

        d=Doctor.objects.filter(specialization=data)
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(DoctorSerializer.data,status=status.HTTP_200_OK)



#APIView for creating AdminUser (admin registration)

class AdminRegister(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)