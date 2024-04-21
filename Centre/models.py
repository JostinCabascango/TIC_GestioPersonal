from django.db import models


class Person(models.Model):
    """
    Base model for Student and Teacher
    """
    name = models.CharField(max_length=100)
    lastname1 = models.CharField(max_length=100)
    lastname2 = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True

    def __str__(self):
        """
        String representation of the person
        :return:  str  -  Person name, lastname1, lastname2, and email
        """
        return f'{self.name} {self.lastname1} {self.lastname2} - {self.email}'


class Course(models.Model):
    """
    Course model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """
        String representation of the course
        :return:  str  -  Course name
        """
        return self.name if self.name else 'Unnamed Course'


class Module(models.Model):
    """
    Module model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Change this line
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the module
        :return:  str  -  Module name
        """
        return self.name if self.name else 'Unnamed Module'


class Student(Person):
    """
    Student model
    """
    courses = models.ManyToManyField(Course)
    modules = models.ManyToManyField(Module)


class Teacher(Person):
    """
    Teacher model
    """
    courses = models.ManyToManyField(Course)
    tutor = models.BooleanField(default=False)
    modules = models.ManyToManyField(Module)
