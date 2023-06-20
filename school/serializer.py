from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'age', 'address', 'date_of_birth', 'father_name',
                  'mother_name', 'parent_phone_number', 'contact_number', 'parent_email', 'gender']


class TeacherSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(read_only=True)
    grade = serializers.CharField(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'email', 'phone_number',
                  'address', 'gender', 'grade', 'subject']
