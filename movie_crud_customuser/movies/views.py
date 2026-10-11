from urllib import response

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializer import MovieSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import generics
from rest_framework.filters import SearchFilter


class RegisterAPIView(APIView):
    def post(self,request):
        serializer_instances=UserSerializer(data=request.data)
        if serializer_instances.is_valid():
            serializer_instances.save()
            return Response(serializer_instances.data)
        else:
            return Response(serializer_instances.errors)


#               Search APIView
class SearchAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[SearchFilter]
    search_fields=['title','director','language']

#                      or

# class SearchAPIView(APIView):
#     def get(self,request):
#         # Fetches data coming from request URL
#         data=self.request.query_params.get('search')
#
#         # Filter movie records having title matching with data
#         m=Movie.objects.filter(Q(title__icontains=data) |
#                                Q(director__icontains=data)|
#                                 Q(language__icontains=data))
#             if not m.exist():
#                 return Response({"message": "No record Found"},status=status.HTTP_200_OK)

        #converts the queryset into native type using serializer class
        # serializer_instances=MovieSerializer(m,many=True)

        # returns response as Json usning Response class
        # return Response(serializer_instances.data,status=status.HTTP_200_OK)







#                        Using ViewSets
from rest_framework import viewsets
class MovieView(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class =MovieSerializer

#                        Generics class
# from rest_framework import generics
# class MovieList(generics.ListAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer

#                       Mixins class
# from rest_framework import mixins,generics
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Movie.objects.all()
#     serializer_class =MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,
#                                mixins.UpdateModelMixin,
#                                mixins.DestroyModelMixin,
#                                generics.GenericAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
#


#                        API View class
# Create your views here.
#GET
#API view for reading all records
# class AllMovies(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)

#POST

# class MovieCreate(APIView):
#     def post(self,request):
#         d=request.data
#         serializer_instance=MovieSerializer(data=d)
#         if serializer_instance.is_valid():
#             # cleaned_data=serializer_instance.validated_data
#             # title=cleaned_data['title']
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#API view read a specific data using ID
# from django.shortcuts import get_object_or_404
# class MovieDetail(APIView):
#     def get(self,request,i):
#         d=get_object_or_404(Movie,id=i)
#         serializer_instance=MovieSerializer(d)
#         if serializer_instance:
#             return Response(serializer_instance.data,status=status.HTTP_200_OK)
#         else:
#             return Response({"message":"Data not found"},status=status.HTTP_400_BAD_REQUEST)
#
# # API full updating
#
# class MovieUpdate(APIView):
#     def put(self,request,i):
#         d=request.data
#         m=Movie.objects.get(id=i)
#         serializer_instance=MovieSerializer(m,data=d)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class MovieDelete(APIView):
#     def delete(self,request,i):
#         m=get_object_or_404(Movie,id=i)
#         m.delete()
#         return Response({"Message":"Data deleted successfully"},status=status.HTTP_301_MOVED_PERMANENTLY)



