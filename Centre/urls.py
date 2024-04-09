from django.urls import path

from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("index", views.index, name="index"),
    path("students", views.students, name="students"),
    path("students/<int:student_id>", views.student_detail, name="student_detail"),
    path("teachers", views.teachers, name="teachers"),
    path("teachers/<int:teacher_id>", views.teacher_detail, name="teacher_detail"),
]
