from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

#Model serializer for user register
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username',
                'password',
                'email',
                'first_name',
                'last_name'
                ]
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u

