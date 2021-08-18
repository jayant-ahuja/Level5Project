from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional

    portfolio_site = models.URLField(blank=True) # user can leave this field empty...
    
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # name of the folder where to upload these images...

    # need to add code to create profile_pics folder using code. Video - creates it manually. => created automatically by django. NO need for explicit creation.

    def __str__(self):
        return self.user.username
    
