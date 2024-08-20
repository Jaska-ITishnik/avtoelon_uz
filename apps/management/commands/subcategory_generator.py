from django.core.management import BaseCommand
from faker import Faker

from apps.models import SubCategory


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("subcategory", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database ...'))

        subcategories = []
        f = Faker()
        for _ in range(options['subcategory']):
            subcategories.append(SubCategory(
                name=f.name(),
                slug=f.slug(),
                category_id=2
            ))
        SubCategory.objects.bulk_create(subcategories)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['subcategory']} subcategories")
        )