from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from Centre.models import Student, Teacher
from .forms import UserRegisterForm, StudentForm, TeacherForm


class AboutView(View):
    def get(self, request):
        return render(request, "Centre/about.html", {})


class IndexView(View):
    def get(self, request):
        context = {
            "teacher": {"name": "John", "lastname": "Doe", "age": 25},
        }
        return render(request, "Centre/index.html", context)


class StudentsView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "Centre/students.html", {"students": students})


class StudentDetailView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        return render(request, "Centre/student_detail.html", {"student": student})


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, "Centre/teachers.html", {"teachers": teachers})


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        return render(request, "Centre/teacher_detail.html", {"teacher": teacher})


class StudentEditView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(instance=student)
        return render(request, 'Centre/student_edit.html', {'form': form, 'student': student})

    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')


class StudentDeleteView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('students')


class TeacherEditView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(instance=teacher)
        return render(request, 'Centre/teacher_edit.html', {'form': form, 'teacher': teacher})

    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')


class TeacherDeleteView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        teacher.delete()
        return redirect('teachers')


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
