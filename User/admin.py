from django.contrib import admin
from User.models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'available')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('account',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'faculty', 'masters_supervisor', 'doctoral_supervisor', 'home_phone', 'office_phone')


@admin.register(Student_Grade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('colledge_code', 'national_code', 'name', 'faculty')


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Student_Class)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('grade', 'major', 'name', 'instructor', 'headmaster', 'campus')


@admin.register(Student_Category)
class StudentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Student)
class StudentCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_class', 'student_category')


@admin.register(Undergraduate)
class StudentCategoryAdmin(admin.ModelAdmin):
    list_display = ('student',)


@admin.register(Postgraduate)
class PostgraduateAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor')


admin.site.site_header = "Easy MicroService for Database"
admin.site.site_title = "Easy Django MicroService for Database"
