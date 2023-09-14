from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    place = models.CharField(max_length=150)


    def __str__(self):
        return self.username
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):

    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField()


    def __str__(self):
        return self.myuser.username


