from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from random import choice
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *

# Create your views here.


class StudentRegister(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def put(self, request, pk):
    #     student = get_object_or_404(Student, pk=pk)
    #     serializer = StudentSerializer(student, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'status': 'success', 'message': 'Student updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)


class StudentEdit(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success', 'message': 'Student updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)


class CreateTeacher(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        grade_choices = [choice(Grade.choices)[0]
                         for _ in range(3)]
        subject_choices = [choice(Subject.choices)[0]
                           for _ in range(3)]

        serializer.save(
            grade=choice(grade_choices),
            subject=choice(subject_choices)
        )


class TeacherEdit(RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success', 'message': 'Teacher updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
