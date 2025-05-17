import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atcproject.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    username = 'khdev'
    password = 'Hh123456Hh'
    email = 'admin@example.com'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully.")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    create_admin()
