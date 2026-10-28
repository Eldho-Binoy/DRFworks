from django.contrib.gis import serializers
from django.shortcuts import render

# Create your views here.

from app.models import Movie
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import MovieSerializer
from rest_framework import status



class MovieCreate(APIView):
    def post(self,request):
        serializer_instance=MovieSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)

class MovieList(APIView):
    def get(self,request):
        qs=Movie.objects.all()
        serializer_instance = MovieSerializer(qs, many=True)
        return Response(serializer_instance.data)

from django.shortcuts import get_object_or_404
# class MovieRetrieve(APIView):
#     def get(self,request,i):
#         qs=get_object_or_404(Movie,id=i)
#         serializer_instance=MovieSerializer(qs)
#         return Response(qs.data)

class MovieRetrieve(APIView):
    def get(self, request, i):
        qs = get_object_or_404(Movie, id=i)
        serializer_instance = MovieSerializer(qs)
        return Response(serializer_instance.data)

class MovieUpdate(APIView):
    def put(self,request,i):
        data=request.data
        e=get_object_or_404(Movie,id=i)
        serializer_instance = MovieSerializer(instance=e, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"created successfully"})
        else:
            return Response(serializer_instance.errors)

class MoviePatch(APIView):
    def patch(self,request,i):
        d=request.data
        e=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(instance=e,data=d,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"done"})
        else:
            return Response(serializer_instance.errors)

class MovieDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Movie,id=i)
        e.delete()
        return Response({"message":"deleted"})