#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Easy_Database_User.settings')
    try:
        print("Try to create a django admin user.")
        user_name = os.getenv('DJANGO_ADMIN_USERNAME')
        user_pwd = os.getenv('DJANGO_ADMIN_PASSWORD')
        user_email = os.getenv('DJANGO_ADMIN_USEREMAIL')
        import django
        django.setup()
        if user_name is not None and user_pwd is not None and user_email is not  None:
            from django.contrib.auth.models import User
            user = User.objects.create(username=user_name, email=user_email, is_superuser=True, is_staff=True)
            user.set_password(user_pwd)
            user.save()
        else:
            print("The required parameters are not in the environment variable and the creation fails.")
    except Exception as e:
        print(e)
        print("Create django admin user fail. Django server will launch without any admin user.")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
