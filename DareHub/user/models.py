from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from datetime import timezone


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set', help_text='Specific permissions for this user.', verbose_name='user permissions')

class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at