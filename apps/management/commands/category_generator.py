from django.core.management import BaseCommand
from faker import Faker

from apps.models import Category


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("category", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database ...'))

        advs = []
        f = Faker()
        for _ in range(options['category']):
            advs.append(Category(
                name=f.name(),
                slug=f.slug()
            ))
        Category.objects.bulk_create(advs)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['category']} categories")
        )