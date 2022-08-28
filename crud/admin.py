from django.contrib import admin
from .models.student import Student
from .models.teacher import Teacher
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)