from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication


# class JWTAccessCookieAuthentication(JWTAuthentication):
#     """Reads JWT access token from an HttpOnly cookie."""

#     def authenticate(self, request):
#         raw_token = request.COOKIES.get(settings.JWT_ACCESS_COOKIE_NAME)
#         if not raw_token:
#             return None
#         validated_token = self.get_validated_token(raw_token)
#         return self.get_user(validated_token), validated_token


from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        
        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token