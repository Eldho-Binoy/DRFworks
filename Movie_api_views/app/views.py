from rest_framework.views import APIView
from app.models import Movie
from app.serializers import MovieSerializer
from rest_framework import status
from rest_framework.response import Response
from app import serializers
#APIview class
# class MovieListCreate(APIView):
#     def post(self,request):
#         serializer_instance=MovieSerializer(data=request.data)
#
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self,request):
#         qs=Movie.objects.all()
#         serializer_instance=MovieSerializer(qs,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)



#Using Mixins

# from rest_framework import mixins,generics
# class MovieListCreate(mixins.ListModelMixin,)




#using Generics

# from rest_framework import mixins,generics
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer




#using Viewsets

from rest_framework import viewsets
class MovieListCreate(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer



#using APIView
from django.shortcuts import get_object_or_404
class MovieRetrieveUpdateDelete(APIView):
    def get(self,request,i):
        e=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(e)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,i):
        data=request.data
        e=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(insatnce=e,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, i):

    # data = request.data
    #         e = get_object_or_404(Movie, id=i)
    #         serializer_instance = MovieSerializer(instance=e, data=data,partial=True)
    #         if serializer_instance.is_valid():
    #             serializer_instance.save()
    #             return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    #     def delete(self,request,i):
    #         e=get_object_or_404(Movie,id=i)
    #         e.delete()
    #         return Response({"message:deleted successfully"},status=status.HTTP_204_NO_CONTENT)

    # USING MIXINS
    # class MovieRetrieveUpdateDestroy(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    #     queryset=Movie.objects.all()
    #     serializer_class=MovieSerializer
    #
    #     def get(self,request,pk):
    #         return self.retrieve(request,pk)
    #
    #     def put(self, request, pk):
    #         return self.update(request, pk)
    #
    #     def patch(self, request, pk):
    #         return self.partial_update(request, pk)
    #
    #     def delete(self, request, pk):
    #         return self.destroy(request, pk)

    # USING GENERICS

    # class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #     queryset=Movie.objects.all()
    #     serializer_class=MovieSerializer

    # USING VIEWSETS

    class MovieView(viewsets.ModelViewSet):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer