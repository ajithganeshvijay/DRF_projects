from rest_framework import serializers
from books.models import Books
# class BooksSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     author=serializers.CharField(max_length=100)
#     price=serializers.IntegerField()
#     pages=serializers.IntegerField()


    # def create(self,validated_data):
    #     l=Books.objects.create(**validated_data)
    #     l.save()
    #     return l
    #
    # def update(self,i,validated_data):
    #     i.title=validated_data.get("title",i.title)
    #     i.author=validated_data.get("author",i.author)
    #     i.price=validated_data.get("price",i.price)
    #     i.pages=validated_data.get("pages",i.pages)
    #
    #     i.save()
    #     return i

# using Model Serializer
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'