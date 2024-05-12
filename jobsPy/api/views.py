from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import serializers
from jobsPy.api.serializers import UserRegistrationSerializer, UserSerializer, CompanyProfileSerializer, \
    JobSeekerSerializer, FavoriteJobSerializer
from ..jobs.models import Job, Applicant, FavoriteJob
from ..jobs.serializers import JobsDetailSerializer, ApplicantSerializer
from ..jobseekers.models import JobSeeker

userModel = get_user_model()

class MyTokenObtainPairView(TokenObtainPairView):
    pass  # Use default implementation

class MyTokenRefreshView(TokenRefreshView):
    pass  # Use default implementation

# class UserRegistrationAPIView(APIView):
#     serializer_class = UserRegistrationSerializer
#
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({'email': user.email}, status=status.HTTP_201_CREATED)

class UserRegistrationAPIView(CreateAPIView):
    queryset = userModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'email': user.email}, status=status.HTTP_201_CREATED)

class MySecuredAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated user can access this endpoint"})


# class UserProfileView(MySecuredAPIView, APIView):
#     # permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user = request.user
#         # You can customize the user data returned based on your requirements
#         return Response({
#             'id': user.id,
#             'email': user.email,
#             'role': user.role,
#             # Add other user data as needed
#         })

class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        email = user.email

        if hasattr(user, 'company'):  # Check if the user has a company profile
            profile_serializer = CompanyProfileSerializer(user.company)
            user_type = 'company'
        elif hasattr(user, 'jobseeker'):  # Check if the user has a job seeker profile
            profile_serializer = JobSeekerSerializer(user.jobseeker)
            user_type = 'jobseeker'
        else:
            return Response({'error': 'User profile not found'}, status=404)

        return Response({'user_type': user_type, 'user': profile_serializer.data, 'email': email})


class JobSeekerUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Retrieve the JobSeeker instance of the current user
        return JobSeeker.objects.get(user=self.request.user)


class JobsDetailsAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobsDetailSerializer
    # permission_classes = (permissions.AllowAny)


@api_view(['POST'])
def apply_for_job(request, pk):
    if request.user.is_authenticated and request.user.role == 'jobseeker':
        try:
            job = Job.objects.get(id=pk)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

        if not Applicant.objects.filter(user=request.user, job=job).exists():
            # Create an Applicant instance and save it to the database
            applicant = Applicant.objects.create(user=request.user, job=job)
            serializer = ApplicantSerializer(applicant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'User has already applied for this job'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

# @api_view(['GET'])
# def job_applicants(request, pk):
#     applicants = Applicant.objects.filter(job_id=pk)
#     serializer = ApplicantSerializer(applicants, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def job_applicants(request, pk):
    # Check if the current user is authenticated
    if request.user.is_authenticated:
        # Filter applicants for the specified job and current user
        try:
            applicant = Applicant.objects.get(job_id=pk, user=request.user)
            serializer = ApplicantSerializer(applicant)
            return Response(serializer.data)
        except Applicant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class AddToFavoritesAPIView(APIView):
    def post(self, request, pk):
        # Get the job object
        job = get_object_or_404(Job, pk=pk)

        # Check if the job is not already in favorites
        if not FavoriteJob.objects.filter(user=request.user, job=job).exists():
            # Create a new FavoriteJob instance
            favorite_job = FavoriteJob.objects.create(user=request.user, job=job)
            serializer = FavoriteJobSerializer(favorite_job)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'message': 'Job is already in favorites'}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromFavoritesAPIView(APIView):
    def post(self, request, pk):
        # Get the job object
        job = get_object_or_404(Job, pk=pk)

        # Check if the job is in favorites for the current user
        favorite_job = FavoriteJob.objects.filter(user=request.user, job=job).first()

        if favorite_job:
            # Job is in favorites, remove it
            favorite_job.delete()
            return Response({'message': 'Job removed from favorites'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'message': 'Job is not in favorites'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_favorite_status(request, pk):
    if not request.user.is_authenticated:
        return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    is_favorite = FavoriteJob.objects.filter(user=request.user, job_id=pk).exists()

    return Response({'is_favorite': is_favorite}, status=status.HTTP_200_OK)