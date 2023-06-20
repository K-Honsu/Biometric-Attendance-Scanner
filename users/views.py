from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        user = serializer.save()
        user.set_password(password)
        user.save()


class UserDetails(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'status': 'success', 'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
