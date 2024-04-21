from django.urls import path
from .views import AboutView, IndexView, StudentsView, StudentDetailView, TeachersView, TeacherDetailView, \
    StudentEditView, StudentDeleteView, TeacherEditView, TeacherDeleteView, RegisterView

urlpatterns = [
    path("about", AboutView.as_view(), name="about"),
    path("index", IndexView.as_view(), name="index"),
    path("students", StudentsView.as_view(), name="students"),
    path("students/<int:student_id>/edit", StudentEditView.as_view(), name="students.edit"),
    path("students/<int:student_id>/delete", StudentDeleteView.as_view(), name="students.delete"),
    path("students/<int:student_id>", StudentDetailView.as_view(), name="student_detail"),
    path("teachers", TeachersView.as_view(), name="teachers"),
    path("teachers/<int:teacher_id>/edit", TeacherEditView.as_view(), name="teachers.edit"),
    path("teachers/<int:teacher_id>/delete", TeacherDeleteView.as_view(), name="teachers.delete"),
    path("teachers/<int:teacher_id>", TeacherDetailView.as_view(), name="teacher_detail"),
    path('register/', RegisterView.as_view(), name='register'),
]
