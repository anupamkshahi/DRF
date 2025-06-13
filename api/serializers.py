from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from .models import Blog, Comment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment   
        fields ='__all__'    

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'          