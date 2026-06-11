import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken

from .models import EmailOTP
from .serializers import RegisterSerializer, LoginSerializer, VerifyOTPSerializer, MeSerializer

User = get_user_model()

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        
        # If the email exists but the user never verified (is_active=False), 
        # delete the old record so they can start fresh.
        if email:
            User.objects.filter(email=email, is_active=False).delete()
            if User.objects.filter(email=email, is_active=True).exists():
                return Response(
                    {"error": "This email is already registered. Please sign in instead."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate 4-digit OTP
            otp_code = str(random.randint(1000, 9999))
            
            # Save OTP in database
            EmailOTP.objects.update_or_create(
                user=user,
                defaults={'otp': otp_code}
            )

            # Send Email
            try:
                send_mail(
                    'Your EduSense Verification Code',
                    f'Your 4-digit code is: {otp_code}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response({"error": "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"message": "User created. OTP sent to email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            
            try:
                otp_record = EmailOTP.objects.get(user__email=email, otp=otp)
                user = otp_record.user
                
                # --- Mark the user as officially verified ---
                user.is_active = True
                user.save()
                
                # Success - Clean up OTP
                otp_record.delete()
                
                response = Response({
                    "message": "Email verified successfully",
                    "user": MeSerializer(user).data
                }, status=status.HTTP_200_OK)
                return response

            except EmailOTP.DoesNotExist:
                return Response({"error": "Invalid OTP or Email"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                user = User.objects.get(email=email)
                if not user.is_active:
                    return Response(
                        {"error": "Please verify your email before logging in."},
                        status=status.HTTP_401_UNAUTHORIZED
                    )

                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    response = Response({
                        "message": "Login successful",
                        "user": MeSerializer(user).data
                    }, status=status.HTTP_200_OK)
                    
                    response.set_cookie(
                        key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                        value=str(refresh.access_token),
                        httponly=True,
                        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                        path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH']
                    )
                    return response
            except User.DoesNotExist:
                pass
                
        return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

class MeView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = MeSerializer(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
        return response
