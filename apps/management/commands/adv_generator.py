from django.core.management import BaseCommand
from faker import Faker

from apps.models import Adv


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("adv", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database ...'))

        advs = []
        f = Faker()
        for _ in range(options['adv']):
            advs.append(Adv(
                is_barging=f.boolean(),
                addition_info=f.text(),
                created_at=f.date(),
                updated_at=f.date(),
                owner_id=1,
                district_id=15,
                region_id=1,
                subcategory_id=1
            ))
        Adv.objects.bulk_create(advs)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['adv']} advertisements")
        )