from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set', help_text='Specific permissions for this user.', verbose_name='user permissions')
