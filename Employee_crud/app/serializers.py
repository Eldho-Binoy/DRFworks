from rest_framework import serializers
from app.models import Employee
class EmployeeSerializer(serializers.Serializer):        #for converting the employeee data we use employeeserializer
    gender_choices = (('male', 'MALE'), ('female', 'FEMALE'))
    empid = serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=gender_choices)
    salary = serializers.IntegerField()
    designation = serializers.CharField(max_length=20)
    joining_date = serializers.DateField(read_only=True)

#after validation and before saving
    def create(self,validated_data):
        print(validated_data)
        e=Employee.objects.create(**validated_data)  #create employee record
        e.save()
        return e