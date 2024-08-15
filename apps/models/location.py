from django.db.models import ForeignKey, CASCADE

from .categories import SlugBase


class Region(SlugBase):
    class Meta:
        db_table = 'regions'


class District(SlugBase):
    region = ForeignKey('apps.Region', CASCADE)

    class Meta:
        db_table = 'districts'
