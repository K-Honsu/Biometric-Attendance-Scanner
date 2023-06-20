from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, fullname, email, password=None):
        if not email:
            raise ValueError('Please enter a valid email address')
        email = self.normalize_email(email)
        username = email
        user = self.model(
            email=email,
            fullname=fullname,
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, fullname, email, password=None):
        user = self.create_user(
            email=email,
            fullname=fullname,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.username = email
        user.save(using=self._db)
        return user


class UserAccount(AbstractUser, PermissionsMixin):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=500, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.fullname
