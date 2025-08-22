from django.shortcuts import render

from rest_framework import generics
from .models import UserSignup
from .serializers import UserSignupSerializer
from .serializers import UserLoginSerializer
from .models import UserLogin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

"""
class UserSignupView(generics.ListCreateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer

class UserSignupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer

    """

# Login view
class UserLoginView(generics.CreateAPIView):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer


# Validator

@api_view(["POST"])
def signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)