from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from patient.serializers import UserSerializer,AppointmentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from patient.models import Appointment
from datetime import datetime,time,timedelta

# Create your views here.
class PatientRegister(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class PatientAppointmentListCreate(APIView):

    permission_classes = [IsAuthenticated]
    authentication_class = [BasicAuthentication]

    def post(self,request):
        data=request.data
        serializer_instance=AppointmentSerializer(data=data)
        if serializer_instance.is_valid():

            data=serializer_instance.validated_data
            d=data['doctor']
            date=data['appointment_date']

            a=Appointment.objects.filter(doctor=d,appointment_date=date).last()
            appointment_time=time(9,0,0)

            if a:
                token_number=a.token_number+1
                appointment_time=(datetime(date,appointment_time)+timedelta(minutes=15)).time()
            else:
                token_number=1

            serializer_instance.save(token_number=token_number,appointment_time=appointment_time)
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)