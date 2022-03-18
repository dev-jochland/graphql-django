from decouple import config
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Create a superuser if none exist
    Example:
        manage.py createsuperuser_if_none_exists
    """

    def handle(self, *args, **options):
        user = get_user_model()
        username = config('DJANGO_ADMIN_USERNAME')
        password = config('DJANGO_ADMIN_PASSWORD')
        email = config('DJANGO_ADMIN_EMAIL')

        if user.objects.filter(username=username).exists():
            return self.stdout.write(f'Local user "{username}" already exists')
        user.objects.create_superuser(username=username, password=password, email=email)
        self.stdout.write(f'Local user "{username}" was created')
