from apps.models import Adv, Category, News, Region, SubCategory, User
from django.core.management import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    faker = Faker()

    def add_arguments(self, parser):
        parser.add_argument('-u', '--users', type=int)
        parser.add_argument('-c', '--category', type=int)
        parser.add_argument('-n', '--news', type=int)
        parser.add_argument('-a', '--adv', type=int)
        parser.add_argument('-s', '--subcategory', type=int)

    def _adv(self, n: int):
        owner = User.objects.order_by('?').first()
        region = Region.objects.order_by('?').first()
        subcategory = Region.objects.order_by('?').first()
        advs = [Adv(
            is_barging=self.faker.boolean(),
            addition_info=self.faker.text(),
            created_at=self.faker.date(),
            updated_at=self.faker.date(),
            owner_id=owner.id,
            district_id=15,
            region_id=region.id,
            subcategory_id=subcategory.id
        ) for _ in range(n)]

        Adv.objects.bulk_create(advs)
        self.stdout.write(self.style.SUCCESS(f"Successfully populated {n} advs"))

    def _users(self, n: int):
        users = [User(
            is_superuser=self.faker.boolean(),
            is_active=self.faker.boolean(),
            is_staff=self.faker.boolean(),
            date_joined=self.faker.date(),
            phone_number=f"998{self.faker.msisdn()[4:]}"
        ) for _ in range(n)]

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f"Successfully populated {n} advs"))

    def _category(self, n: int):
        categories = [
            Category(
                name=self.faker.name(),
                slug=self.faker.slug()
            ) for _ in range(n)
        ]

        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS(f"Successfully populated {n} categories"))

    def _subcategory(self, n: int):
        category = Category.objects.order_by('?').first()
        subcategories = [SubCategory(
            name=self.faker.name(),
            slug=self.faker.slug(),
            category_id=category.id
        ) for _ in range(n)]

        SubCategory.objects.bulk_create(subcategories)
        self.stdout.write(self.style.SUCCESS(f"Successfully populated {n} subcategories"))

    def _news(self, n: int):
        author = User.objects.order_by('?').first()
        news = [
            News(
                content=self.faker.text(),
                author_id=author.id,
                photo=self.faker.file_name(extension='png'),
                title=self.faker.text(),
                slug=self.faker.slug()
            ) for _ in range(n)
        ]
        News.objects.bulk_create(news)
        self.stdout.write(self.style.SUCCESS(f"Successfully populated {n} news"))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database ...'))
        methods = {'users', 'category', 'news', 'adv', 'subcategory'}
        for method in methods:
            options[method] and getattr(self, f"_{method}")(options[method])
        self.stdout.write(self.style.SUCCESS(f"Successfully populated databases"))

        #
        # if options.get('category'):
        #     self._category(options['category'])
        #
        # if options.get('subcategory'):
        #     self._subcategory(options['subcategory'])
        #
        # if options.get('news'):
        #     self._news(options['news'])
        #
        # if options.get('users'):
        #     self._users(options['users'])
        #
        # if options.get('adv'):
        #     self._adv(options['adv'])
