from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="dutch@123.com",  # harry_potter@123.com ,  dutch@123.com
            first_name="dutch",
            last_name="butch",
            is_staff=True,
            is_superuser=False
        )
        user.set_password("12345")
        user.save()