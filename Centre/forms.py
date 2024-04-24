from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Centre.models import Student, Module, Teacher, Course


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'lastname1', 'lastname2', 'email', 'courses', 'modules']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description', 'duration', 'course']


class StudentModuleForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['modules']


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['courses']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'lastname1', 'lastname2', 'email', 'courses', 'tutor', 'modules']


class TeacherModuleForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['modules']


class TeacherCourseForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['courses']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
