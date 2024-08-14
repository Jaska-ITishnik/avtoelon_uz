import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.models import News


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("new", type=int)

    def handle(self, *args, **options):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS('Populating database ...'))

        news = []
        f = Faker()
        for _ in range(options['new']):
            news.append(News(
                content=f.text(),
                author_id=1,
                image=f.file_extension(),
                title=f.text()
            ))
        News.objects.bulk_create(news)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated {options['new']} users")
        )