from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser, OTP
from random import randint
from datetime import timedelta
from django.utils import timezone
from .emails import send_otp_via_email


def generate_otp_code():
    return randint(100000, 999999)
@receiver(post_save, sender=CustomUser)
def  send_signup_email(sender, instance, created, *args, **kwargs):
    if not created:
        return
    
    if not instance.email:
        return
    
    code = generate_otp_code()
    expire_time = timezone.now() + timedelta(minutes=5)
    OTP.objects.create(user=instance, code=code, expires_at=expire_time)

    try:
        send_otp_via_email(instance.email, code)
    except Exception as e:
        import logging
        logging.exception(f"failed to send OTP email to {instance.email}: {e}")