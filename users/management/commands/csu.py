from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    This command is used to create initial users for the application.
    It creates four users: an admin, two patients, and two doctors.
    Each user is created with default values and passwords set to '123'.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@bk.com',
            # first_name='Admin_first_name',
            # last_name='Admin_last_name',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('123')
        user.save()
