from django.shortcuts import render, redirect
from Centre.models import Student, Teacher
from .forms import UserRegisterForm


def about(request):
    """
    About view function that renders the about.html template
    :param request:
    :return:  render  -  about.html template
    """
    return render(request, "Centre/about.html", {})


def index(request):
    """
    Index view function that renders the index.html template
    :param request:
    :return:  render  -  index.html template
    """
    context = {
        "teacher": {"name": "John", "lastname": "Doe", "age": 25},
    }
    return render(request, "Centre/index.html", context)


def students(request):
    """
    Students view function that renders the students.html template
    :param request:
    :return:  render  -  students.html template
    """
    students = Student.objects.all()
    return render(request, "Centre/students.html", {"students": students})


def student_detail(request, student_id):
    """
    Student detail view function that renders the student_detail.html template
    :param request:
    :param student_id:  int  -  Student id
    :return:  render  -  student_detail.html template
    """
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return render(request, "Centre/errors/student_not_found.html")
    return render(request, "Centre/student_detail.html", {"student": student})


def teachers(request):
    """
    Teachers view function that renders the teachers.html template
    :param request:
    :return:  render  -  teachers.html template
    """
    teachers = Teacher.objects.all()
    return render(request, "Centre/teachers.html", {"teachers": teachers})


def teacher_detail(request, teacher_id):
    """
    Teacher detail view function that renders the teacher_detail.html template
    :param request:
    :param teacher_id:  int  -  Teacher id
    :return:  render  -  teacher_detail.html template
    """
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return render(request, "Centre/errors/teacher_not_found.html")
    return render(request, "Centre/teacher_detail.html", {"teacher": teacher})


def student_edit(request):
    return None


def student_delete(request):
    return None


def teacher_edit(request):
    return None


def teacher_delete(request):
    return None


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
