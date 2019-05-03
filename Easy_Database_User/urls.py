"""Easy_Database_User URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Easy_Database_User.settings")
django.setup()

from rest_framework.routers import DefaultRouter
from User.views import *

router = DefaultRouter()
router.register('account', AccountService)
router.register('user', UserService)
router.register('faculty', FacultyService)
router.register('teacher', TeacherService)
router.register('student', StudentGradeService)
router.register('major', MajorService)
router.register('campus', CampusService)
router.register('student_class', StudentClassService)
router.register('student_category', StudentCategoryService)
router.register('student', StudentService)
router.register('undergraduate', UndergraduateService)
router.register('graduate', GraduateService)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
