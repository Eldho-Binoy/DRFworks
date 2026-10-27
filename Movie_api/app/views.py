from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import MovieSerializer
from app import serializers
from rest_framework.response import Response
from app.models import Movie

# Create your views here.
class Moviecreate(APIView):
    def post(self,request):
        serializer_instance=MoviesSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"craeted"})

        else:
            return Response(serializer_instance.errors)