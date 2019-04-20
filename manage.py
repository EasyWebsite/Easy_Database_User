#!/usr/bin/env python
import os
import sys


def start_nameko_servieces():
    try:
        print("Try to start nameko services.")
        from nameko.runners import ServiceRunner
        from User import views
        runner = ServiceRunner(config={'AMQP_URI': 'pyamqp://guest:guest@localhost'})
        runner.add_service(views.AccountService)
        runner.add_service(views.UserService)
        runner.add_service(views.FacultyService)
        runner.add_service(views.TeacherService)
        runner.add_service(views.StudentGradeService)
        runner.add_service(views.MajorService)
        runner.add_service(views.CampusService)
        runner.add_service(views.StudentClassService)
        runner.add_service(views.StudentCategoryService)
        runner.add_service(views.StudentService)
        runner.add_service(views.UndergraduateService)
        runner.add_service(views.GraduateService)
        runner.start()
    except Exception as e:
        print(e)
        raise Exception("Start nameko services failed. Django server will still start soon normally.")


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Easy_Database_User.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
