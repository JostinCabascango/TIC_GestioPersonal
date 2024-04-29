from django.urls import path

from Centre.views import AboutView, IndexView, RegisterView, StudentsView, StudentDetailView, StudentEditView, \
    StudentDeleteView, TeachersView, TeacherEditView, TeacherDetailView, TeacherDeleteView, TeacherCreateView, \
    StudentCreateView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("", IndexView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),

    path("students/", StudentsView.as_view(), name="students"),
    path("students/create/", StudentCreateView.as_view(), name="students.create"),
    path("students/<int:student_id>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/<int:student_id>/edit/", StudentEditView.as_view(), name="students.edit"),
    path("students/<int:student_id>/delete/", StudentDeleteView.as_view(), name="students.delete"),

    path("teachers/", TeachersView.as_view(), name="teachers"),
    path("teachers/create/", TeacherCreateView.as_view(), name="teachers.create"),
    path("teachers/<int:teacher_id>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("teachers/<int:teacher_id>/edit/", TeacherEditView.as_view(), name="teachers.edit"),
    path("teachers/<int:teacher_id>/delete/", TeacherDeleteView.as_view(), name="teachers.delete"),
]
