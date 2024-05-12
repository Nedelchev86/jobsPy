from django.urls import path

from jobsPy.api.views import UserRegistrationAPIView, MyTokenObtainPairView, MyTokenRefreshView, UserProfileView, \
    JobSeekerUpdateAPIView, JobsDetailsAPIView, apply_for_job, job_applicants, AddToFavoritesAPIView, \
    RemoveFromFavoritesAPIView, check_favorite_status
from jobsPy.blog.views import BlogPostListCreateAPIView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint to obtain JWT token
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('blog/', BlogPostListCreateAPIView.as_view(), name='blog-list'),
    path('user/', UserProfileView.as_view(), name='user-profile'),
    path('user/jobseeker/update/', JobSeekerUpdateAPIView.as_view(), name='jobseeker-update'),
    path('jobs/<int:pk>/', JobsDetailsAPIView.as_view(), name='jobs-details'),
    path('jobs/<int:pk>/apply/', apply_for_job, name="apply-job"),
    path('jobs/<int:pk>/applicants/', job_applicants, name='job_applicants'),
    path('jobs/<int:pk>/favorite/add/', AddToFavoritesAPIView.as_view(), name='add_to_favorites'),
    path('jobs/<int:pk>/favorite/remove/', RemoveFromFavoritesAPIView.as_view(), name='remove_from_favorites'),
    path('jobs/<int:pk>/favorite/check/', check_favorite_status, name='check_favorite_status'),
]
