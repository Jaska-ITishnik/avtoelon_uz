from django.db.models import Model, ForeignKey, CASCADE, CharField, ManyToManyField


class Category(Model):
    name = CharField(max_length=20, unique=True)

    # slug

    class Meta:
        db_table = 'category'


class SubCategory(Model):
    name = CharField(max_length=20, unique=True)
    category = ForeignKey('apps.Category', CASCADE)
    fields = ManyToManyField('apps.Field', blank=True)


class Field(Model):
    pass
    # name
    # is_required
    # type
    # help_text
