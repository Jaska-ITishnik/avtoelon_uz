from django.core.management import BaseCommand
from faker import Faker

from apps.models import User


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("users", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database ...'))

        users = []
        f = Faker()
        for _ in range(options['users']):
            users.append(User(
                is_superuser=f.boolean(),
                is_staff=f.boolean(),
                date_joined=f.date(),
                phone_number=f"998{f.msisdn()[4:]}"
            ))
        User.objects.bulk_create(users)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['users']} users")
        )