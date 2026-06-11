import random
from django.core.mail import send_mail


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):
    subject = 'Your OTP Verification'

    message = f'Your OTP is: {otp}'

    send_mail(
        subject,
        message,
        'yourmail@gmail.com',
        [email],
        fail_silently=False,
    )