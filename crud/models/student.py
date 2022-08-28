from django.db import models
from .teacher import *
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, blank = True)
    email = models.EmailField(null=True, blank=True)
    contact_Number = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='students/',null=True, blank=True)

    def __str__(self):
        return(self.name)



