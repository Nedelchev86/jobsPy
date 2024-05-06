from django.urls import path

from jobsPy.api.views import UserRegistrationAPIView, MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint to obtain JWT token
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
]
