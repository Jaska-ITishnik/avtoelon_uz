from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
)
from django.utils.text import slugify


class SlugBase(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    class Meta:
        abstract = True


class Category(SlugBase):
    pass


class SubCategory(SlugBase):
    category = ForeignKey('apps.Category', CASCADE)
    fields = ManyToManyField('apps.Field', blank=True)


class Field(Model):
    name = CharField(max_length=255)
    is_required = BooleanField(default=False)
    # name
    # is_required
    # type
    # help_text
