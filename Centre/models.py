from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    modules = models.TextField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    tutor = models.BooleanField(default=False)
    modules = models.TextField()
