from rest_framework import serializers
from movies.models import Movie
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['username',
                 'password',
                 'email',
                 'first_name',
                 'last_name',
                 ]

    #to create user account we use USer.objects.create_user for password hashing
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u
# class MovieSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     director = serializers.CharField(max_length=40)
#     language = serializers.CharField(max_length=30)
#     year = serializers.IntegerField()
#     rating = serializers.FloatField()
#     run_time = serializers.IntegerField()
#     image=serializers.ImageField()
                                #null is used to interfere the error if there is no image is inserted
#
class MovieSerializer(serializers.ModelSerializer):
    class Meta:  #inline class(default)
        model = Movie
        fields = '__all__' #it included ID and all datas from table

        #or
        # fields=['title','director'.....]  without ID it using specific data

        
    # def create(self,validated_data):
    #     m=Movie.objects.create(**validated_data)
    #     return m
    #
    # def update(self,i,validate_data):
    #     i.title=validate_data.get("title",i.title)
    #     i.director=validate_data.get("director",i.director)
    #     i.language=validate_data.get("language",i.language)
    #     i.year=validate_data.get("year",i.year)
    #     i.rating=validate_data.get("rating",i.rating)
    #     i.run_time=validate_data.get("run_time",i.run_time)
    #
    #     i.save()
    #     return i




