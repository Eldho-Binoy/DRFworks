from rest_framework import serializers
from app.models import Employee
# class EmployeeSerializer(serializers.Serializer):        #for converting the employeee data we use employeeserializer
#     # id=serializers
#     gender_choices = (('male', 'MALE'), ('female', 'FEMALE'))
#     empid = serializers.IntegerField()
#     name = serializers.CharField(max_length=10)
#     age = serializers.IntegerField()
#     gender = serializers.ChoiceField(choices=gender_choices)
#     salary = serializers.IntegerField()
#     designation = serializers.CharField(max_length=20)
#     place = serializers.CharField(max_length=100)
#     joining_date = serializers.DateField(read_only=True)
#
# #after validation and before saving
#     def create(self,validated_data):
#         print(validated_data)
#         e=Employee.objects.create(**validated_data)  #create employee record
#         e.save()
#         return e
#
#     def update(self,instance,validated_data):
#         # e.empid=validated_data['empid']
#         e.empid=validated_data.get('empid',e.empid)
#         e.empid = validated_data.get('name', e.name)
#         e.empid = validated_data.get('empid', e.empid)
#         e.empid = validated_data.get('age', e.age)
#         e.empid = validated_data.get('gender', e.gender)
#         e.empid = validated_data.get('salary', e.salary)
#         e.empid = validated_data.get('designation', e.designation)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        read_only_fields=['id','joining_date']


def Validate(self,data):
    if data['age'] <= 0:
        raise serializers.ValidationError("Age shoiuld be positive")

    return data