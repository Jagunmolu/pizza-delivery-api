from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('Email should be provided'))

        email=self.normalize_email(email)

        new_user=self.model(email=email,**extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superadmin', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_('Superuser should have is_staff as True'))

        if not extra_fields.get('is_superadmin'):
            raise ValueError(_('Superuser should have is_superadmin as True'))

        if not extra_fields.get('is_active'):
            raise ValueError(_('Superuser should have is_active as True'))

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):

    username=models.CharField(max_length=25,unique=True)
    email=models.EmailField(unique=True)
    phone_number=PhoneNumberField(null=False, unique=True)

    USERNAME_FIELD='username'

    REQUIRED_FIELDS=['email','phone_number']

    objects=CustomUserManager()

    def __str__(self):
        return f'<User {self.username}'