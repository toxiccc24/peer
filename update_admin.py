import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atcproject.settings')
django.setup()

from django.contrib.auth.models import User

def update_admin():
    username = 'khdev'
    password = 'Hh123456Hh'
    email = 'admin@example.com'

    try:
        user = User.objects.get(username=username)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.email = email
        user.save()
        print(f"Superuser '{username}' updated successfully.")
    except User.DoesNotExist:
        print(f"User '{username}' does not exist. Please run create_admin.py to create the user first.")

if __name__ == '__main__':
    update_admin()
