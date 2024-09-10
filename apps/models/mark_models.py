from django.db.models import CASCADE, ForeignKey, JSONField

from .categories import SlugBase


class MarkModels(SlugBase):
    subcategory_field = ForeignKey('apps.Field', on_delete=CASCADE)
    mark_models = JSONField(default=dict)
