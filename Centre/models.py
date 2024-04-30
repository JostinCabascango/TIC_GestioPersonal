from django.db import models

ROLE_STUDENT = 'ST'
ROLE_TEACHER = 'TE'
ROLE_CHOICES = [
    (ROLE_STUDENT, 'Student'),
    (ROLE_TEACHER, 'Teacher'),
]


class Person(models.Model):
    """
    Base model for Student and Teacher
    """
    first_name = models.CharField(max_length=100)
    first_lastname = models.CharField(max_length=100)
    second_lastname = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        """
        String representation of the person
        :return:  str  -  Person name, lastname1, lastname2, and email
        """
        return f'Name: {self.first_name} {self.first_lastname} {self.second_lastname}, Email: {self.email}, Role: {self.get_role_display()}'


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
        return f'Course: {self.name}, Description: {self.description}'


class Module(models.Model):
    """
    Module model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the module
        :return:  str  -  Module name
        """
        return f'Module: {self.name}, Description: {self.description}, Duration: {self.duration} hours'


class Student(Person):
    """
    Student model
    """
    courses = models.ManyToManyField(Course)
    modules = models.ManyToManyField(Module)

    def save(self, *args, **kwargs):
        self.role = ROLE_STUDENT
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the student
        :return:  str  -  Full name, email, role and number of courses and modules
        """
        return f'{super().__str__()}, Courses: {self.courses.count()}, Modules: {self.modules.count()}'


class Teacher(Person):
    """
    Teacher model
    """
    courses = models.ManyToManyField(Course)
    tutor = models.BooleanField(default=False)
    modules = models.ManyToManyField(Module)

    def save(self, *args, **kwargs):
        self.role = ROLE_TEACHER
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the teacher
        :return:  str  -  Full name, email, role, tutor, number of courses and modules
        """
        tutor_status = "Tutor" if self.tutor else "Not a tutor"
        return f'{super().__str__()}, {tutor_status}, Courses: {self.courses.count()}, Modules: {self.modules.count()}'
