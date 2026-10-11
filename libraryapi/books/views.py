from asyncio import start_server

from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter

from rest_framework.views import APIView

from books import serializer
from books.models import Book
from rest_framework.response import Response
from rest_framework import status, response, authentication

from books.serializer import BookSerializer
from books.serializer import UserSerializer
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#                             (login)TokenAPIView

class GetToken(APIView):
    def get(self,request):
        data=request.data
        u=data['username']
        p=data['password']
        user=authenticate(username=u,password=p)

        if user:
            token,created=Token.objects.get_or_create(user=user)
            return JsonResponse({'Token':token.key})

        else:
            return JsonResponse({"Message":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)


#                               ListCreate APIView
class BookListCreate(APIView):
         authentication_classes = [TokenAuthentication]
         permission_classes = [IsAuthenticated]
         def get(self,request):
             l=Book.objects.all()
             serializer_instances=BookSerializer(l,many=True)
             return Response(serializer_instances.data)

         def post(self,request):
             d=request.data
             serializer_instances=BookSerializer(data=d)
             if serializer_instances.is_valid():
                 serializer_instances.save()
                 return Response(serializer_instances.data,status=status.HTTP_200_OK)
             else:
                 return Response(status=status.HTTP_400_BAD_REQUEST)


#                           RetrieveUpdateDelete APIView
class BookRetrieveUpdateDelete(APIView):
        authentication_classes = [TokenAuthentication]
        permission_classes=[IsAuthenticated]
        def get(self,request,i):
            d=request.data
            l=Book.objects.get(id=i)
            serializer_instances=BookSerializer(l,data=d)
            if serializer_instances.is_valid():
                serializer_instances.save()
                return Response(serializer_instances.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        def put(self,request,i):
            d=request.data
            l=Book.objects.get(id=i)
            serializer_instances=BookSerializer(l,data=d)
            if serializer_instances.is_valid():
                serializer_instances.save()
                return Response(serializer_instances.data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        def delete(self,request,i):
                l=Book.objects.get(id=i)
                l.delete()
                return Response({"Message":"Deleted Successfully"})

#                           UserRegister APIView
class UserRegister(APIView):
    def post(self,request):
        d=request.data
        serializer_instances=UserSerializer(data=d)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#                              Search APIVIew
class BookSearch(APIView):
    def get(self,request):
        data=self.request.query_params.get('search')
        l=Book.objects.filter(Q(title__icontains=data)|
                              Q(author__icontains=data)|
                              Q(language__icontains=data))
        if not l:
            return Response({"Invalid credential"},status=status.HTTP_400_BAD_REQUEST)
        serializer_instances=BookSerializer(l,many=True)
        return Response(serializer_instances.data,status=status.HTTP_200_OK)

#                                   Logout API

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({"Message":"Logout Successfully"})










