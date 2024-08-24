from django.db.models import ForeignKey, CASCADE

from .categories import SlugBase


class Region(SlugBase):
    pass


class District(SlugBase):
    region = ForeignKey('apps.Region', CASCADE)
