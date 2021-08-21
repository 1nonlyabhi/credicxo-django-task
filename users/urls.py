from django.urls import path
from .views import RegisterView, UserAPIView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('manage', UserAPIView.as_view())
]