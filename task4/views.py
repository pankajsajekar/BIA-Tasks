from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.
class UserListCreateAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UserLoginView(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'authenticatedUser': {
                    'data': serializer.data,
                }
            }
            return Response(response, status=status_code)