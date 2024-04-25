from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    name= models.CharField(max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=16, blank=True)
    address = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)

    education = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()


