from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Address=models.TextField()
    Profile_Pic=models.ImageField(upload_to='pp')

    def __str__(self):
        return self.Address