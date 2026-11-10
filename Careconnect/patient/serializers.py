
from rest_framework import serializers
from django.contrib.auth.models import User
from patient.models import Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        u.save()
        return u

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'
        read_only_fields=['id','appointment_time','created','token_number']

    def validate(self,data):
        d=data['doctor']
        date=data['appointment_date']
        a=Appointment.objects.filter(doctor=d,appointment_date=date).last()
        if a.token_number==25:
            raise serializers.ValidationError("slots are full")