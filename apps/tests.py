# import json
#
# with open('fixtures/districts.json', 'r') as f:
#     regions = json.load(f)
#     for i in regions:
#         # i['pk'] = i['id']
#         # del i['id']
#         i["model"] = "apps.district"
#         # i['fields'] = {'name': i['name'], 'region_id':i["region_id"]}
#         # del i['name']
#         # del i["region_id"]
#     with open('fixtures/districts.json', 'w') as f:
#         json.dump(regions, f, indent=2)

from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from faker import Faker


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        fake = Faker()

        for poll_id in options["poll_ids"]:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
            )
