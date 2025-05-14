from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager



class CustomUser(AbstractUser,PermissionsMixin):

    profile_picture = models.ImageField(upload_to="profile_pictures",verbose_name="Profile Picture",null=True,blank=True)
    last_seen = models.DateTimeField(auto_now=True,verbose_name="Last Seen",null=True,blank=True)