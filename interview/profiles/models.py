
from django.db import models
from django import forms
from interview.core.behaviors import TimestampedModel
from django.contrib.auth.models import AbstractUser

# I am having trouble with my local setup getting this repo running
# normally I would use django startapp command to auto create the profiles app.  For the sake of time I just manually 
# created these files in order to complete the coding challenge
class UserProfile(AbstractUser, TimestampedModel, models.Model):
    username = models.CharField(default=AbstractUser.email)
    is_admin = models.BooleanField()
    avatar = models.ImageField()

    # the following fields are already defined on the AbstractUser model and will be inherited
    # first_name = models.CharField(max_length=150, blank=True)
    # last_name = models.CharField(max_length=150, blank=True)
    # email = models.EmailField(blank=True)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # date_joined = models.DateTimeField()
    # password = models.CharField(max_length=128)
    # last_login = models.DateTimeField(blank=True, null=True)
    # is_active: bool | BooleanField[Any] = ...
    # is_superuser = models.BooleanField()

    def get_full_name(self) -> str:
        return f'{self.first_name} - {self.last_name}'
    
    def get_username(self) -> str:
        return f'{self.username}'
    
    def is_authenticated(self) -> str:
        return f'{self.username}'
