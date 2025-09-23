from django.core.mail import send_mail
from django.conf import settings

def send_otp_via_email(to_email, code):
    subject="OTP"
    message=f"Your OTP is {code}"
    from_email=settings.EMAIL_HOST_USER
    send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])