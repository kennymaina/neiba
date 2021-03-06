from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Neiba(models.Model):
    name = models.CharField(max_length =30)
    location=models.CharField(max_length =30)
    population = models.IntegerField()
    image = models.ImageField(upload_to = 'images/')


class Profile(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Profile'
    def create_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()