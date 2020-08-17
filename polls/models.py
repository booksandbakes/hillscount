from django.db import models

# Create your models here.
class register(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=20,primary_key=True,unique=True)
    Password=models.CharField(max_length=20)
    City=models.CharField(max_length=30)
    def __str__(self):
        return self.Username
    
