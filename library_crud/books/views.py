from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from books import serializer
from books.serializer import BooksSerializer
from books.models import Books
from rest_framework import status
from rest_framework import generics
from rest_framework.filters import SearchFilter


# Create your views here.
#for SEARCH APIView

# class BookSearch(generics.ListAPIView):
#     queryset=Books.objects.all()
#     serializer_class=BooksSerializer
#     filter_backends=[SearchFilter]
#
#     SearchFilter=['title','author']
#                   or

class BookSearch(APIView):
    def get(self,request):
        data=self.request.query_params.get('search')
        l=Books.objects.filter(title__icontains=data)
        serializer_instances=BooksSerializer(l,many=True)
        return Response(serializer_instances.data,status=status.HTTP_200_OK)


#API view based
class AllBooks(APIView):
    def get(self,request):
        s=Books.objects.all()
        serializer_instances=BooksSerializer(s,many=True)

        return Response(serializer_instances.data)


class BookCreate(APIView):
    def post(self,request):
        d=request.data
        serializer_instances=BooksSerializer(data=d)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data)
        else:
            return Response(serializer_instances.errors)


class Bookdetail(APIView):
    def get(self,request,i):
        l=Books.objects.get(id=i)
        serializer_instances=BooksSerializer(l)
        if serializer_instances:
            return Response(serializer_instances.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404
class BookUpdate(APIView):
    def put(self,request,i):
        b=get_object_or_404(Books,id=i)
        d=request.data
        serializer_instances=BooksSerializer(b,data=d)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data)
        else:
            return Response(serializer_instances.errors)


class BookPartialUpdate(APIView):
    def patch(self,request,i):
        b=get_object_or_404(Books,id=i)
        d=request.data
        serializer_instances=BooksSerializer(b,data=d)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data)
        else:
            return Response(serializer_instances.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDelete(APIView):
    def delete(self,request,i):
        b=Books.objects.get(id=i)
        b.delete()
        return Response({"Message":"Deletion successfully"})




