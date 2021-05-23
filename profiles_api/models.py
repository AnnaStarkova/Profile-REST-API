from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        # set to the model manager is for (in our case UserProfile)
        user = self.model(email=email, name=name)
        # password must be encrypted
        user.set_password(password)
        # saving proccess in django
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """create and save new superuser(admin) with wider rights"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database for user in the system"""
    # user column with emal mxa_lenght = 255, unique email adrees in the database
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # permission system
    # all activated
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # model manager - custom one
    objects = UserProfileManager()

    # to work with django admin
    # username and email are required to be authorized
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string repr of user"""
        return self.email
