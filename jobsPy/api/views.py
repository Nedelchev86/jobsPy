from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from jobsPy.api.serializers import UserRegistrationSerializer

userModel = get_user_model()

class MyTokenObtainPairView(TokenObtainPairView):
    pass  # Use default implementation

class MyTokenRefreshView(TokenRefreshView):
    pass  # Use default implementation

class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'email': user.email}, status=status.HTTP_201_CREATED)



class MySecuredAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated user can access this endpoint"})