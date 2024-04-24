from django.contrib.auth.mixins import LoginRequiredMixin
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
        return render(request, "Centre/students/students.html", {"students": students})


class StudentDetailView(View):
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return render(request, "Centre/errors/object_not_found.html",
                          {"object_id": student_id, "object_type": "Student", "object_list_url": "students"})
        return render(request, "Centre/students/student_detail.html", {"student": student})


class StudentEditView(LoginRequiredMixin, View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(instance=student)
        return render(request, 'Centre/students/student_edit.html', {'form': form, 'student': student})

    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')


class StudentDeleteView(LoginRequiredMixin, View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        return_url = 'students'
        return render(request, 'Centre/Modal/confirm_delete.html', {'object': student, 'return_url': return_url})

    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return_url = 'students'
        return redirect(return_url)


class StudentCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'Centre/students/student_create.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, "Centre/teachers/teachers.html", {"teachers": teachers})


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return render(request, "Centre/errors/object_not_found.html",
                          {"object_id": teacher_id, "object_type": "Teacher", "object_list_url": "teachers"})
        return render(request, "Centre/teachers/teacher_detail.html", {"teacher": teacher})


class TeacherEditView(LoginRequiredMixin, View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(instance=teacher)
        return render(request, 'Centre/teachers/teacher_edit.html', {'form': form, 'teacher': teacher})

    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')


class TeacherDeleteView(LoginRequiredMixin, View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        return_url = 'teachers'
        return render(request, 'Centre/Modal/confirm_delete.html', {'object': teacher, 'return_url': return_url})

    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        teacher.delete()
        return_url = 'teachers'
        return redirect(return_url)


class TeacherCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TeacherForm()
        return render(request, 'Centre/teachers/teacher_create.html', {'form': form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        else:
            return render(request, 'Centre/teachers/teacher_create.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
