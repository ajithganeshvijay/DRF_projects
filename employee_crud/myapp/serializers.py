from rest_framework import serializers
from myapp.models import Employee
class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    gender_choice=[
        ('male','Male'),('female','Female') #('DB value','display value')
    ]
    gender=serializers.ChoiceField(choices=gender_choice)
    salary=serializers.IntegerField()
    joining_date=serializers.DateField()
    designation=serializers.CharField(max_length=20)
    image=serializers.ImageField()

    def create(self,validated_data):
        e=Employee.objects.create(**validated_data)
        return e

    def update(self,i,validated_data):
        i.empid=validated_data.get("empid",i.empid)
        i.name=validated_data.get("name",i.name)
        i.age=validated_data.get("age",i.age)
        i.gender=validated_data.get("gender",i.gender)
        i.salary=validated_data.get("salary",i.salary)
        i.designation=validated_data.get("designation",i.designation)

        i.save()
        return i

    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError("Age must be positive")

        elif data['age']<18:
            return serializers.ValidationError("Age must be greater than 18")

        return data
