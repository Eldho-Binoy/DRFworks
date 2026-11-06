
from rest_framework import serializers
from doctor.models import Doctor
from django.contrib.auth.models import User

class DoctorSerializer(serializers.ModelSerializer):
    class Meta: #for providing description about serializer class
        model=Doctor
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

    def create(self, validated_data):
        u = User.objects.create_superuser(**validated_data)
        u.save()
        return u