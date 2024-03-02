from django.urls import path

from jobsPy.main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

]
