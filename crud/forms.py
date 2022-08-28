from dataclasses import field
from django import forms
from .models import student,teacher

class StudentForm(forms.ModelForm):
    class Meta():
        model = student.Student
        fields = "__all__"

class TeacherForm(forms.ModelForm):
    class Meta():
        model = teacher.Teacher
        fields = "__all__"
