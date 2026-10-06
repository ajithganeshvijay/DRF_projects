from urllib import response

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

#GET
#API view for reading all records
class AllMovies(APIView):
    def get(self,request):
        m=Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#POST

class MovieCreate(APIView):
    def post(self,request):
        d=request.data
        serializer_instance=MovieSerializer(data=d)
        if serializer_instance.is_valid():
            # cleaned_data=serializer_instance.validated_data
            # title=cleaned_data['title']
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#API view read a specific data using ID
from django.shortcuts import get_object_or_404
class MovieDetail(APIView):
    def get(self,request,i):
        d=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(d)
        if serializer_instance:
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Data not found"},status=status.HTTP_400_BAD_REQUEST)

# API full updating

class MovieUpdate(APIView):
    def put(self,request,i):
        d=request.data
        m=Movie.objects.get(id=i)
        serializer_instance=MovieSerializer(m,data=d)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class MovieDelete(APIView):
    def delete(self,request,i):
        m=get_object_or_404(Movie,id=i)
        m.delete()
        return Response({"Message":"Data deleted successfully"},status=status.HTTP_301_MOVED_PERMANENTLY)