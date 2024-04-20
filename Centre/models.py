from django.db import models


class Student(models.Model):
    """
    Student model
    """
    name = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    modules = models.TextField()

    def __str__(self):
        """
        String representation of the student
        :return:  str  -  Student name, lastname1, lastname2, and email
        """
        return f'{self.name} {self.lastname1} {self.lastname2} - {self.email}'


class Teacher(models.Model):
    """
    Teacher model
    """
    name = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    tutor = models.BooleanField(default=False)
    modules = models.TextField()

    def __str__(self):
        """
        String representation of the teacher
        :return:  str  -  Teacher name, lastname1, lastname2, and email
        """
        return f'{self.name} {self.lastname1} {self.lastname2} - {self.email}'
