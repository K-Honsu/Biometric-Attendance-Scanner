from django.urls import path
from . import views

urlpatterns = [
    path('student-reg/', views.StudentRegister.as_view()),
    path('student-detail/<uuid:pk>/', views.StudentEdit.as_view()),
    path('teacher-reg/', views.CreateTeacher.as_view()),
    path('teacher-detail/<int:pk>/',
         views.TeacherEdit.as_view()),
]
