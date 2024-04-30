from django.contrib import admin
from .models import Course, Module, Student, Teacher


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname1', 'lastname2', 'email')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration', 'course')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'first_name', 'second_lastname', 'email', 'role')
    filter_horizontal = ('courses', 'modules')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'first_name', 'second_lastname', 'email', 'tutor', 'role')
    filter_horizontal = ('courses', 'modules')


# admin.site.register(Person, PersonAdmin)  # Commented out
admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
