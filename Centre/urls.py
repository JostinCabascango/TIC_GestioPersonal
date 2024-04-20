from django.urls import path

from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("index", views.index, name="index"),
    path("students", views.students, name="students"),
    path("students/<int:student_id>/edit", views.student_edit, name="students.edit"),
    path("students/<int:student_id>/delete", views.student_delete, name="students.delete"),
    path("students/<int:student_id>", views.student_detail, name="student_detail"),
    path("teachers", views.teachers, name="teachers"),
    path("teachers/<int:teacher_id>/edit", views.teacher_edit, name="teachers.edit"),
    path("teachers/<int:teacher_id>/delete", views.teacher_delete, name="teachers.delete"),
    path("teachers/<int:teacher_id>", views.teacher_detail, name="teacher_detail"),
    path('register/', views.register, name='register'),

]
