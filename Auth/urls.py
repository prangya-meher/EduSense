from django.urls import path
from .views import RegisterView, VerifyOTPView, LoginView, LogoutView, MeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('verify-otp/', VerifyOTPView.as_view(), name='auth-verify'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
    path('me/', MeView.as_view(), name='auth-me'),
]