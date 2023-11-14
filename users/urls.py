from users.apps import UsersConfig
from django.urls import path

from users.views import (LoginView, LogoutView, RegisterView, VerificationView, ErrorVerificationView,
                         GenerateNewPasswordView, ProfileView)
app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/', VerificationView.as_view(), name='verify_email'),
    path('verify_email/error/', ErrorVerificationView.as_view(), name='verify_email_error'),
    path('generate_new_password/', GenerateNewPasswordView.as_view(), name='generate_password'),
    path('profile/', ProfileView.as_view(), name='profile')
]
