import uuid
from django.db import models
from .enums import *
from django.contrib.auth import get_user_model
User = get_user_model()


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=450)
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    parent_phone_number = models.CharField(max_length=15)
    contact_number = models.CharField(max_length=15)
    parent_email = models.EmailField(unique=True)
    gender = models.CharField(choices=Gender.choices, max_length=6)
    # fingerprint =

    def __str__(self):
        return f'Student is {self.user}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=150)
    address = models.CharField(max_length=450)
    gender = models.CharField(choices=Gender.choices, max_length=6)
    grade = models.CharField(choices=Grade.choices, max_length=6)
    subject = models.CharField(choices=Subject.choices, max_length=20)


class Attendance(models.Model):
    attendance = models.CharField(
        choices=Attendance.choices, max_length=6, default='absent')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
